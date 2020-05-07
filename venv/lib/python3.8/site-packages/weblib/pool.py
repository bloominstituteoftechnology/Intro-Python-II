from concurrent.futures import ProcessPoolExecutor, ThreadPoolExecutor
from traceback import format_exc

POOL_RESET_PERIOD = 10000
POOL_TASK_CHUNK = 1000


class PoolError(Exception):
    pass


def process_in_pool(handler, task_iterator, thread_pool=False,
                    pool_reset_period=POOL_RESET_PERIOD,
                    pool_task_chunk=POOL_TASK_CHUNK):
    pool = None
    futs = []
    count = 0

    while True:
        if pool is None or not count % pool_reset_period:
            if pool is not None:
                pool.shutdown()
            if thread_pool:
                pool = ThreadPoolExecutor(max_workers=1)
            else:
                pool = ProcessPoolExecutor()
            print('Pool has reseted')

        futs = []
        for x in range(pool_task_chunk):
            count += 1
            try:
                item = next(task_iterator)
            except StopIteration:
                break
            else:
                fut = pool.submit(handler, *item)
                futs.append(fut)
        print('Submited %d tasks into pool' % len(futs))

        if not futs:
            break

        for fut in futs:
            try:
                yield fut.result()
            except Exception as ex:
                yield PoolError(ex, format_exc())
