is_magician = False
is_expert = False

# check if magician AND expert: 'You are a master magician'

# Check if magician but not expert 'At least you're getting there'

# if you're not a magician: 'You need magic powers'


if is_expert and is_magician:
    print('You are a master magician')

elif is_magician and not is_expert:
    print('At least you\'re getting there')

elif not is_magician:
    print('You need magic powers')
