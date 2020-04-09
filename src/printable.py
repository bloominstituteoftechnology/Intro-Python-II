############################################################
#   PRINTABLE
############################################################


class printable:

    @staticmethod
    def to_str(o, attr_keys):

        class_name = o.__class__.__name__

        attr_entries = (
            f'    {attr_key}: {repr(getattr(o, attr_key))}'
            for attr_key in attr_keys
        )

        return ('\n'.join((
            f'{class_name} {{',
            *attr_entries,
            '}',
        )))
        # -- I really don't like the hanging non-indentation in multi-line strings...

    @staticmethod
    def to_repr(o, attr_keys):

        class_name = o.__class__.__name__

        attr_values = (repr(getattr(o, attr)) for attr in attr_keys)

        return (
            f'{class_name}({", ".join(attr_values)})'
        )
