from common.database import db

tags_posts = db.Table('tags_posts',
                        db.Column('tag_id', db.Integer, db.ForeignKey('tags.id')),
                        db.Column('post_id', db.Integer, db.ForeignKey('posts.id'))
                        )