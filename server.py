import imaging_server_kit as sk
import skimage.data


@sk.algorithm
def hello_world():
    return sk.Notification("Hello world!")

# Note: You can copy your algorithms here and
# serve them instead of `hello_world`!
# ...

if __name__=='__main__':
    sk.serve(hello_world)