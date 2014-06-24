WITH_ADMIN = True


from bottle import route, default_app

# This must be added in order to do correct path lookups for the views
import os
from bottle import TEMPLATE_PATH
TEMPLATE_PATH.append(os.path.join(os.environ['OPENSHIFT_REPO_DIR'], 'wsgi/views/')) 

import routes

if WITH_ADMIN:
    import admin
    
application=default_app()
