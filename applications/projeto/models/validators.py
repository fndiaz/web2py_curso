
Post.blog.requires = IS_IN_DB(db, 'blog.id', "%(title)s")

Post.title.requires = [IS_NOT_EMPTY(error_message=T("Esta vazio!")),
                       IS_NOT_IN_DB(db, 'post.title', error_message=T("title already exists"))]

Post.category.requires = IS_IN_DB(db, 'category.id', "%(name)s", multiple=True)