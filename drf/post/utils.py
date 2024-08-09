import os


def user_main_image_post_upload(instance, filename):
    return os.path.join("post",instance.user.username,  instance.title ,"main_pic", filename)


def user_image_post_upload(instance, filename):
    return os.path.join("post",instance.post.user.username,  instance.post.title ,"post_pics", filename)