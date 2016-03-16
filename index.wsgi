from huaban import wsgi 
import sae 
application = sae.create_wsgi_app(wsgi.application) 