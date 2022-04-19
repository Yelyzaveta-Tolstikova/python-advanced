# Create Category
Category.objects.create(name='Cat_1')

# Create Post
Post.objects.create(title='post_1', text='text_1', category_id=1)

# Update or set Category for Post
cat = Category.objects.get(name='Cat_2')
post = Post.objects.get(title='post_4')
post.category = cat
post.save()

# Updated Post title
post = Post.objects.get(title='post_1')
post.title = 'post_new_name_1'
post.save()

# Update Category for particular Posts
post = Post.objects.filter(pk__gte=3)
post.update(category_id=1)

# Search Posts by Category
cat = Category.objects.get(name='Cat_2')
Post.objects.filter(category=cat)

# Get Posts by title
Post.objects.get(title='post_2')

# Search Posts by year/month of date published
Post.objects.filter(date_published__year='2022')
Post.objects.filter(date_published__month='04')

# Search Posts which not in a particular Category
cat = Category.objects.get(name='Cat_3')
Post.objects.exclude(category=cat)


# Search Posts by Category and order results by title reversed
Post.objects.filter(category_id=2).order_by('-title')

# Count of Posts in Category
cat = Category.objects.get(name='Cat_2')
Post.objects.filter(category=cat).count()

# Count of Posts published in a particular month
Post.objects.filter(date_published__month='04').count()
