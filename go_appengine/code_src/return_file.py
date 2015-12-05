def USER(user=None):
	if not user:
		return {}
	else:
		user = {'username': user.username, 'auth': user.auth}
		return user

def SUCCESS():
	return {'status': True}