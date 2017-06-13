import twitter

all_accounts = twitter.get_all_accounts()
if len(all_accounts) >= 1:
	account = all_accounts[0]

text = 'Your Text⁣'
twitter.post_tweet(account, text, parameters=None)
while text < '⁣(Your Text)⁣⁣⁣⁣⁣':
		twitter.post_tweet(account, text, parameters=None)
		text += '⁣'
