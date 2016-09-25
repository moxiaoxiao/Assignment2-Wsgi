

server_root = "./www"
def app(environ, start_response):
	response_headers = [('Content-Type','text/html')]
	start_response('200 OK',response_headers)
	uri = environ['PATH_INFO']
	return get_response_from_uri(uri)
	
def get_response_from_uri(uri):
	if uri.endswith('.html'):
		try:
			_file = open(server_root+uri,'r')
		except Exception as e:
			_file = open(server_root+"/404.html",'r')
		html = _file.readlines()
		out = [line for line in html]
		return out
			
	elif uri == '/' or '':
		return get_response_from_uri('/index.html')
	else:
		method = uri[1:]
		return ["<title>method hello</title>","Hello " + method]