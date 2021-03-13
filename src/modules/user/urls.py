from django.urls import path, re_path
from .conf import *
from .controllers.registerController import OauthRegister as registerHandler
#from .controllers.oauthLoginController import OauthLogin as oauthHandler
#from .controllers.oauthLoginController import OauthRenewLogin as oauthRefreshHandler
#from .controllers.oauthLoginController import OauthLogout as oauthLogoutHandler

#from .controllers.jwtLoginController import JwtLogin as jwtHandler
#from .controllers.jwtLoginController import JwtRenewLogin as jwtRefreshHandler

from .controllers.basicLoginController import BasicLogin as basicHandler
from .controllers.basicLoginController import BasicLogout as basicLogoutHandler

app_name = Config.app_name

urlpatterns = [
  #  re_path(r'^register/?$', registerHandler.as_view(), name="register"),
   # re_path(r'^login/oauth/?$',  oauthHandler.as_view()),
   # re_path(r'^login/renew/?$',  oauthRefreshHandler.as_view()),
  #  path('login/jwt/token/', jwtHandler.as_view(), name='token_obtain_pair'),
   # path('login/jwt/renew/', jwtRefreshHandler.as_view(), name='token_refresh'),

path('login/basic/token/', basicHandler.as_view()),
path('login/basic/logout/', basicLogoutHandler.as_view()),
#re_path(r'^logout/?$',  oauthLogoutHandler.as_view())
]