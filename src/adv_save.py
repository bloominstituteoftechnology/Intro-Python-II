#file i/o functions for historical results
def load_results():
    text_file = open(save_file, "r")
    history = text_file.read().split(",")
    text_file.close()
    return history

def save_results( w, t, l):
    text_file = open(save_file, "w")
    text_file.write( str(w) + "," + str(t) + "," + str(l))
    text_file.close()
