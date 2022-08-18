from django.urls import path
from .views import *

app_name = "post"

urlpatterns = [
    path('index/', post_index, name='index'),
    path('<slug:slug>', post_detail, name='detail'),
    path('create/', post_create, name="create"),
    # path('<slug:slug>/update', post_update, name="update"),
    path('update/<slug:slug>', post_update, name="update"),
    # path('<slug:slug>/delete', post_delete, name="delete"),
    path('delete/<slug:slug>/', post_delete, name="delete"),
    path('myposts/', my_posts, name="myposts")

]
#
# {'environ': {'ALLUSERSPROFILE': 'C:\\ProgramData', 'APPDATA': 'C:\\Users\\MUSTAFA MERT\\AppData\\Roaming',
#              'BRB': 'C:\\Program Files\\HP\\Sure Click\\bin', 'BRS': 'C:\\Program Files\\HP\\Sure Click\\servers',
#              'COMMONPROGRAMFILES': 'C:\\Program Files\\Common Files',
#              'COMMONPROGRAMFILES(X86)': 'C:\\Program Files (x86)\\Common Files',
#              'COMMONPROGRAMW6432': 'C:\\Program Files\\Common Files', 'COMPUTERNAME': 'DESKTOP-0DPGLST',
#              'COMSPEC': 'C:\\WINDOWS\\system32\\cmd.exe', 'DJANGO_SETTINGS_MODULE': 'blog.settings',
#              'DRIVERDATA': 'C:\\Windows\\System32\\Drivers\\DriverData', 'HOMEDRIVE': 'C:',
#              'HOMEPATH': '\\Users\\MUSTAFA MERT', 'IDEA_INITIAL_DIRECTORY': 'C:\\Users\\MUSTAFA MERT\\Desktop',
#              'INTEL_DEV_REDIST': 'C:\\Program Files (x86)\\Common Files\\Intel\\Shared Libraries\\',
#              'LOCALAPPDATA': 'C:\\Users\\MUSTAFA MERT\\AppData\\Local', 'LOGONSERVER': '\\\\DESKTOP-0DPGLST',
#              'MIC_LD_LIBRARY_PATH': 'C:\\Program Files (x86)\\Common Files\\Intel\\Shared Libraries\\compiler\\lib\\mic',
#              'NUMBER_OF_PROCESSORS': '8', 'ONEDRIVE': 'C:\\Users\\MUSTAFA MERT\\OneDrive',
#              'ONLINESERVICES': 'Online Services', 'OS': 'Windows_NT',
#              'PATH': 'C:\\Users\\MUSTAFA MERT\\Desktop\\blog\\venv\\Scripts;C:\\ProgramData\\Oracle\\Java\\javapath;C:\\Program Files (x86)\\Common Files\\Intel\\Shared Libraries\\redist\\intel64\\compiler;C:\\Program Files\\Eclipse Foundation\\jdk-8.0.302.8-hotspot\\bin;C:\\Program Files\\Common Files\\Oracle\\Java\\javapath;C:\\WINDOWS\\system32;C:\\WINDOWS;C:\\WINDOWS\\System32\\Wbem;C:\\WINDOWS\\System32\\WindowsPowerShell\\v1.0\\;C:\\WINDOWS\\System32\\OpenSSH\\;C:\\Program Files\\Microsoft SQL Server\\130\\Tools\\Binn\\;C:\\Program Files\\Microsoft SQL Server\\Client SDK\\ODBC\\170\\Tools\\Binn\\;C:\\Program Files (x86)\\Microsoft SQL Server\\150\\Tools\\Binn\\;C:\\Program Files\\Microsoft SQL Server\\150\\Tools\\Binn\\;C:\\Program Files\\Microsoft SQL Server\\150\\DTS\\Binn\\;C:\\Program Files (x86)\\Microsoft SQL Server\\150\\DTS\\Binn\\;C:\\Program Files\\Azure Data Studio\\bin;C:\\Program Files\\dotnet\\;C:\\Users\\MUSTAFA MERT\\AppData\\Local\\Programs\\Python\\Python310\\Scripts\\;C:\\Users\\MUSTAFA MERT\\AppData\\Local\\Programs\\Python\\Python310\\;C:\\Users\\MUSTAFA MERT\\AppData\\Local\\Programs\\Python\\Python39\\Scripts\\;C:\\Users\\MUSTAFA MERT\\AppData\\Local\\Programs\\Python\\Python39\\;C:\\Users\\MUSTAFA MERT\\AppData\\Local\\Microsoft\\WindowsApps;;C:\\Program Files\\Azure Data Studio\\bin;C:\\Users\\MUSTAFA MERT\\.dotnet\\tools;C:\\Users\\MUSTAFA MERT\\AppData\\Local\\Programs\\Microsoft VS Code\\bin',
#              'PATHEXT': '.COM;.EXE;.BAT;.CMD;.VBS;.VBE;.JS;.JSE;.WSF;.WSH;.MSC', 'PLATFORMCODE': 'AN',
#              'PROCESSOR_ARCHITECTURE': 'AMD64',
#              'PROCESSOR_IDENTIFIER': 'Intel64 Family 6 Model 142 Stepping 12, GenuineIntel', 'PROCESSOR_LEVEL': '6',
#              'PROCESSOR_REVISION': '8e0c', 'PROGRAMDATA': 'C:\\ProgramData', 'PROGRAMFILES': 'C:\\Program Files',
#              'PROGRAMFILES(X86)': 'C:\\Program Files (x86)', 'PROGRAMW6432': 'C:\\Program Files',
#              'PROMPT': '(venv) $P$G',
#              'PSMODULEPATH': 'C:\\Program Files\\WindowsPowerShell\\Modules;C:\\WINDOWS\\system32\\WindowsPowerShell\\v1.0\\Modules;C:\\Program Files (x86)\\Microsoft SQL Server\\150\\Tools\\PowerShell\\Modules\\',
#              'PTSMINSTALLPATH': 'c:\\Program Files\\HP\\HP ProtectTools Security Manager\\Bin\\',
#              'PTSMINSTALLPATH_X86': 'c:\\Program Files (x86)\\HP\\HP ProtectTools Security Manager\\Bin\\',
#              'PUBLIC': 'C:\\Users\\Public', 'PYCHARM_DISPLAY_PORT': '63342', 'PYCHARM_HOSTED': '1',
#              'PYTHONIOENCODING': 'UTF-8',
#              'PYTHONPATH': 'C:\\Users\\MUSTAFA MERT\\Desktop\\blog;C:\\Users\\MUSTAFA MERT\\AppData\\Local\\JetBrains\\Toolbox\\apps\\PyCharm-P\\ch-0\\221.5921.27\\plugins\\python\\helpers\\pycharm_matplotlib_backend;C:\\Users\\MUSTAFA MERT\\AppData\\Local\\JetBrains\\Toolbox\\apps\\PyCharm-P\\ch-0\\221.5921.27\\plugins\\python\\helpers\\pycharm_display',
#              'PYTHONUNBUFFERED': '1', 'REGIONCODE': 'EMEA', 'SESSIONNAME': 'Console', 'SYSTEMDRIVE': 'C:',
#              'SYSTEMROOT': 'C:\\WINDOWS', 'TEMP': 'C:\\Users\\MUSTAF~1\\AppData\\Local\\Temp',
#              'TMP': 'C:\\Users\\MUSTAF~1\\AppData\\Local\\Temp', 'USERDOMAIN': 'DESKTOP-0DPGLST',
#              'USERDOMAIN_ROAMINGPROFILE': 'DESKTOP-0DPGLST', 'USERNAME': 'MUSTAFA MERT',
#              'USERPROFILE': 'C:\\Users\\MUSTAFA MERT', 'VIRTUAL_ENV': 'C:\\Users\\MUSTAFA MERT\\Desktop\\blog\\venv',
#              'WINDIR': 'C:\\WINDOWS', 'ZES_ENABLE_SYSMAN': '1',
#              '_OLD_VIRTUAL_PATH': 'C:\\ProgramData\\Oracle\\Java\\javapath;C:\\Program Files (x86)\\Common Files\\Intel\\Shared Libraries\\redist\\intel64\\compiler;C:\\Program Files\\Eclipse Foundation\\jdk-8.0.302.8-hotspot\\bin;C:\\Program Files\\Common Files\\Oracle\\Java\\javapath;C:\\WINDOWS\\system32;C:\\WINDOWS;C:\\WINDOWS\\System32\\Wbem;C:\\WINDOWS\\System32\\WindowsPowerShell\\v1.0\\;C:\\WINDOWS\\System32\\OpenSSH\\;C:\\Program Files\\Microsoft SQL Server\\130\\Tools\\Binn\\;C:\\Program Files\\Microsoft SQL Server\\Client SDK\\ODBC\\170\\Tools\\Binn\\;C:\\Program Files (x86)\\Microsoft SQL Server\\150\\Tools\\Binn\\;C:\\Program Files\\Microsoft SQL Server\\150\\Tools\\Binn\\;C:\\Program Files\\Microsoft SQL Server\\150\\DTS\\Binn\\;C:\\Program Files (x86)\\Microsoft SQL Server\\150\\DTS\\Binn\\;C:\\Program Files\\Azure Data Studio\\bin;C:\\Program Files\\dotnet\\;C:\\Users\\MUSTAFA MERT\\AppData\\Local\\Programs\\Python\\Python310\\Scripts\\;C:\\Users\\MUSTAFA MERT\\AppData\\Local\\Programs\\Python\\Python310\\;C:\\Users\\MUSTAFA MERT\\AppData\\Local\\Programs\\Python\\Python39\\Scripts\\;C:\\Users\\MUSTAFA MERT\\AppData\\Local\\Programs\\Python\\Python39\\;C:\\Users\\MUSTAFA MERT\\AppData\\Local\\Microsoft\\WindowsApps;;C:\\Program Files\\Azure Data Studio\\bin;C:\\Users\\MUSTAFA MERT\\.dotnet\\tools;C:\\Users\\MUSTAFA MERT\\AppData\\Local\\Programs\\Microsoft VS Code\\bin',
#              '_OLD_VIRTUAL_PROMPT': '$P$G', 'RUN_MAIN': 'true', 'SERVER_NAME': 'DESKTOP-0DPGLST',
#              'GATEWAY_INTERFACE': 'CGI/1.1', 'SERVER_PORT': '8000', 'REMOTE_HOST': '', 'CONTENT_LENGTH': '',
#              'SCRIPT_NAME': '', 'SERVER_PROTOCOL': 'HTTP/1.1', 'SERVER_SOFTWARE': 'WSGIServer/0.2',
#              'REQUEST_METHOD': 'GET', 'PATH_INFO': '/myposts/myposts/', 'QUERY_STRING': '', 'REMOTE_ADDR': '127.0.0.1',
#              'CONTENT_TYPE': 'text/plain', 'HTTP_HOST': 'localhost:8000', 'HTTP_CONNECTION': 'keep-alive',
#              'HTTP_SEC_CH_UA': '".Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103"',
#              'HTTP_SEC_CH_UA_MOBILE': '?0', 'HTTP_SEC_CH_UA_PLATFORM': '"Windows"',
#              'HTTP_UPGRADE_INSECURE_REQUESTS': '1',
#              'HTTP_USER_AGENT': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36',
#              'HTTP_ACCEPT': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
#              'HTTP_SEC_FETCH_SITE': 'none', 'HTTP_SEC_FETCH_MODE': 'navigate', 'HTTP_SEC_FETCH_USER': '?1',
#              'HTTP_SEC_FETCH_DEST': 'document', 'HTTP_ACCEPT_ENCODING': 'gzip, deflate, br',
#              'HTTP_ACCEPT_LANGUAGE': 'tr-TR,tr;q=0.9,en-US;q=0.8,en;q=0.7',
#              'HTTP_COOKIE': 'csrftoken=pYTOrsEiPdANFEXpeR5byys9vyp1KCDk5gprVUDxSlVE0OTMD0QNtpyOvVDgaArl; sessionid=hqv75csqcrtjp2q9tp8ea31re5fcm72s',
#              'wsgi.input': < django.core.handlers.wsgi.LimitedStream object at
#  0x0000027842E74EB0 >, 'wsgi.errors': < _io.TextIOWrapper
# name = '<stderr>'
# mode = 'w'
# encoding = 'utf-8' >, 'wsgi.version': (1,
#                                        0), 'wsgi.run_once': False, 'wsgi.url_scheme': 'http', 'wsgi.multithread': True, 'wsgi.multiprocess': False, 'wsgi.file_wrapper': <
#
# class 'wsgiref.util.FileWrapper'>, 'CSRF_COOKIE': 'pYTOrsEiPdANFEXpeR5byys9vyp1KCDk5gprVUDxSlVE0OTMD0QNtpyOvVDgaArl'
#
# }, 'path_info': '/myposts/myposts/', 'path': '/myposts/myposts/', 'META': {'ALLUSERSPROFILE': 'C:\\ProgramData',
#                                                                            'APPDATA': 'C:\\Users\\MUSTAFA MERT\\AppData\\Roaming',
#                                                                            'BRB': 'C:\\Program Files\\HP\\Sure Click\\bin',
#                                                                            'BRS': 'C:\\Program Files\\HP\\Sure Click\\servers',
#                                                                            'COMMONPROGRAMFILES': 'C:\\Program Files\\Common Files',
#                                                                            'COMMONPROGRAMFILES(X86)': 'C:\\Program Files (x86)\\Common Files',
#                                                                            'COMMONPROGRAMW6432': 'C:\\Program Files\\Common Files',
#                                                                            'COMPUTERNAME': 'DESKTOP-0DPGLST',
#                                                                            'COMSPEC': 'C:\\WINDOWS\\system32\\cmd.exe',
#                                                                            'DJANGO_SETTINGS_MODULE': 'blog.settings',
#                                                                            'DRIVERDATA': 'C:\\Windows\\System32\\Drivers\\DriverData',
#                                                                            'HOMEDRIVE': 'C:',
#                                                                            'HOMEPATH': '\\Users\\MUSTAFA MERT',
#                                                                            'IDEA_INITIAL_DIRECTORY': 'C:\\Users\\MUSTAFA MERT\\Desktop',
#                                                                            'INTEL_DEV_REDIST': 'C:\\Program Files (x86)\\Common Files\\Intel\\Shared Libraries\\',
#                                                                            'LOCALAPPDATA': 'C:\\Users\\MUSTAFA MERT\\AppData\\Local',
#                                                                            'LOGONSERVER': '\\\\DESKTOP-0DPGLST',
#                                                                            'MIC_LD_LIBRARY_PATH': 'C:\\Program Files (x86)\\Common Files\\Intel\\Shared Libraries\\compiler\\lib\\mic',
#                                                                            'NUMBER_OF_PROCESSORS': '8',
#                                                                            'ONEDRIVE': 'C:\\Users\\MUSTAFA MERT\\OneDrive',
#                                                                            'ONLINESERVICES': 'Online Services',
#                                                                            'OS': 'Windows_NT',
#                                                                            'PATH': 'C:\\Users\\MUSTAFA MERT\\Desktop\\blog\\venv\\Scripts;C:\\ProgramData\\Oracle\\Java\\javapath;C:\\Program Files (x86)\\Common Files\\Intel\\Shared Libraries\\redist\\intel64\\compiler;C:\\Program Files\\Eclipse Foundation\\jdk-8.0.302.8-hotspot\\bin;C:\\Program Files\\Common Files\\Oracle\\Java\\javapath;C:\\WINDOWS\\system32;C:\\WINDOWS;C:\\WINDOWS\\System32\\Wbem;C:\\WINDOWS\\System32\\WindowsPowerShell\\v1.0\\;C:\\WINDOWS\\System32\\OpenSSH\\;C:\\Program Files\\Microsoft SQL Server\\130\\Tools\\Binn\\;C:\\Program Files\\Microsoft SQL Server\\Client SDK\\ODBC\\170\\Tools\\Binn\\;C:\\Program Files (x86)\\Microsoft SQL Server\\150\\Tools\\Binn\\;C:\\Program Files\\Microsoft SQL Server\\150\\Tools\\Binn\\;C:\\Program Files\\Microsoft SQL Server\\150\\DTS\\Binn\\;C:\\Program Files (x86)\\Microsoft SQL Server\\150\\DTS\\Binn\\;C:\\Program Files\\Azure Data Studio\\bin;C:\\Program Files\\dotnet\\;C:\\Users\\MUSTAFA MERT\\AppData\\Local\\Programs\\Python\\Python310\\Scripts\\;C:\\Users\\MUSTAFA MERT\\AppData\\Local\\Programs\\Python\\Python310\\;C:\\Users\\MUSTAFA MERT\\AppData\\Local\\Programs\\Python\\Python39\\Scripts\\;C:\\Users\\MUSTAFA MERT\\AppData\\Local\\Programs\\Python\\Python39\\;C:\\Users\\MUSTAFA MERT\\AppData\\Local\\Microsoft\\WindowsApps;;C:\\Program Files\\Azure Data Studio\\bin;C:\\Users\\MUSTAFA MERT\\.dotnet\\tools;C:\\Users\\MUSTAFA MERT\\AppData\\Local\\Programs\\Microsoft VS Code\\bin',
#                                                                            'PATHEXT': '.COM;.EXE;.BAT;.CMD;.VBS;.VBE;.JS;.JSE;.WSF;.WSH;.MSC',
#                                                                            'PLATFORMCODE': 'AN',
#                                                                            'PROCESSOR_ARCHITECTURE': 'AMD64',
#                                                                            'PROCESSOR_IDENTIFIER': 'Intel64 Family 6 Model 142 Stepping 12, GenuineIntel',
#                                                                            'PROCESSOR_LEVEL': '6',
#                                                                            'PROCESSOR_REVISION': '8e0c',
#                                                                            'PROGRAMDATA': 'C:\\ProgramData',
#                                                                            'PROGRAMFILES': 'C:\\Program Files',
#                                                                            'PROGRAMFILES(X86)': 'C:\\Program Files (x86)',
#                                                                            'PROGRAMW6432': 'C:\\Program Files',
#                                                                            'PROMPT': '(venv) $P$G',
#                                                                            'PSMODULEPATH': 'C:\\Program Files\\WindowsPowerShell\\Modules;C:\\WINDOWS\\system32\\WindowsPowerShell\\v1.0\\Modules;C:\\Program Files (x86)\\Microsoft SQL Server\\150\\Tools\\PowerShell\\Modules\\',
#                                                                            'PTSMINSTALLPATH': 'c:\\Program Files\\HP\\HP ProtectTools Security Manager\\Bin\\',
#                                                                            'PTSMINSTALLPATH_X86': 'c:\\Program Files (x86)\\HP\\HP ProtectTools Security Manager\\Bin\\',
#                                                                            'PUBLIC': 'C:\\Users\\Public',
#                                                                            'PYCHARM_DISPLAY_PORT': '63342',
#                                                                            'PYCHARM_HOSTED': '1',
#                                                                            'PYTHONIOENCODING': 'UTF-8',
#                                                                            'PYTHONPATH': 'C:\\Users\\MUSTAFA MERT\\Desktop\\blog;C:\\Users\\MUSTAFA MERT\\AppData\\Local\\JetBrains\\Toolbox\\apps\\PyCharm-P\\ch-0\\221.5921.27\\plugins\\python\\helpers\\pycharm_matplotlib_backend;C:\\Users\\MUSTAFA MERT\\AppData\\Local\\JetBrains\\Toolbox\\apps\\PyCharm-P\\ch-0\\221.5921.27\\plugins\\python\\helpers\\pycharm_display',
#                                                                            'PYTHONUNBUFFERED': '1',
#                                                                            'REGIONCODE': 'EMEA',
#                                                                            'SESSIONNAME': 'Console',
#                                                                            'SYSTEMDRIVE': 'C:',
#                                                                            'SYSTEMROOT': 'C:\\WINDOWS',
#                                                                            'TEMP': 'C:\\Users\\MUSTAF~1\\AppData\\Local\\Temp',
#                                                                            'TMP': 'C:\\Users\\MUSTAF~1\\AppData\\Local\\Temp',
#                                                                            'USERDOMAIN': 'DESKTOP-0DPGLST',
#                                                                            'USERDOMAIN_ROAMINGPROFILE': 'DESKTOP-0DPGLST',
#                                                                            'USERNAME': 'MUSTAFA MERT',
#                                                                            'USERPROFILE': 'C:\\Users\\MUSTAFA MERT',
#                                                                            'VIRTUAL_ENV': 'C:\\Users\\MUSTAFA MERT\\Desktop\\blog\\venv',
#                                                                            'WINDIR': 'C:\\WINDOWS',
#                                                                            'ZES_ENABLE_SYSMAN': '1',
#                                                                            '_OLD_VIRTUAL_PATH': 'C:\\ProgramData\\Oracle\\Java\\javapath;C:\\Program Files (x86)\\Common Files\\Intel\\Shared Libraries\\redist\\intel64\\compiler;C:\\Program Files\\Eclipse Foundation\\jdk-8.0.302.8-hotspot\\bin;C:\\Program Files\\Common Files\\Oracle\\Java\\javapath;C:\\WINDOWS\\system32;C:\\WINDOWS;C:\\WINDOWS\\System32\\Wbem;C:\\WINDOWS\\System32\\WindowsPowerShell\\v1.0\\;C:\\WINDOWS\\System32\\OpenSSH\\;C:\\Program Files\\Microsoft SQL Server\\130\\Tools\\Binn\\;C:\\Program Files\\Microsoft SQL Server\\Client SDK\\ODBC\\170\\Tools\\Binn\\;C:\\Program Files (x86)\\Microsoft SQL Server\\150\\Tools\\Binn\\;C:\\Program Files\\Microsoft SQL Server\\150\\Tools\\Binn\\;C:\\Program Files\\Microsoft SQL Server\\150\\DTS\\Binn\\;C:\\Program Files (x86)\\Microsoft SQL Server\\150\\DTS\\Binn\\;C:\\Program Files\\Azure Data Studio\\bin;C:\\Program Files\\dotnet\\;C:\\Users\\MUSTAFA MERT\\AppData\\Local\\Programs\\Python\\Python310\\Scripts\\;C:\\Users\\MUSTAFA MERT\\AppData\\Local\\Programs\\Python\\Python310\\;C:\\Users\\MUSTAFA MERT\\AppData\\Local\\Programs\\Python\\Python39\\Scripts\\;C:\\Users\\MUSTAFA MERT\\AppData\\Local\\Programs\\Python\\Python39\\;C:\\Users\\MUSTAFA MERT\\AppData\\Local\\Microsoft\\WindowsApps;;C:\\Program Files\\Azure Data Studio\\bin;C:\\Users\\MUSTAFA MERT\\.dotnet\\tools;C:\\Users\\MUSTAFA MERT\\AppData\\Local\\Programs\\Microsoft VS Code\\bin',
#                                                                            '_OLD_VIRTUAL_PROMPT': '$P$G',
#                                                                            'RUN_MAIN': 'true',
#                                                                            'SERVER_NAME': 'DESKTOP-0DPGLST',
#                                                                            'GATEWAY_INTERFACE': 'CGI/1.1',
#                                                                            'SERVER_PORT': '8000', 'REMOTE_HOST': '',
#                                                                            'CONTENT_LENGTH': '', 'SCRIPT_NAME': '',
#                                                                            'SERVER_PROTOCOL': 'HTTP/1.1',
#                                                                            'SERVER_SOFTWARE': 'WSGIServer/0.2',
#                                                                            'REQUEST_METHOD': 'GET',
#                                                                            'PATH_INFO': '/myposts/myposts/',
#                                                                            'QUERY_STRING': '',
#                                                                            'REMOTE_ADDR': '127.0.0.1',
#                                                                            'CONTENT_TYPE': 'text/plain',
#                                                                            'HTTP_HOST': 'localhost:8000',
#                                                                            'HTTP_CONNECTION': 'keep-alive',
#                                                                            'HTTP_SEC_CH_UA': '".Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103"',
#                                                                            'HTTP_SEC_CH_UA_MOBILE': '?0',
#                                                                            'HTTP_SEC_CH_UA_PLATFORM': '"Windows"',
#                                                                            'HTTP_UPGRADE_INSECURE_REQUESTS': '1',
#                                                                            'HTTP_USER_AGENT': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36',
#                                                                            'HTTP_ACCEPT': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
#                                                                            'HTTP_SEC_FETCH_SITE': 'none',
#                                                                            'HTTP_SEC_FETCH_MODE': 'navigate',
#                                                                            'HTTP_SEC_FETCH_USER': '?1',
#                                                                            'HTTP_SEC_FETCH_DEST': 'document',
#                                                                            'HTTP_ACCEPT_ENCODING': 'gzip, deflate, br',
#                                                                            'HTTP_ACCEPT_LANGUAGE': 'tr-TR,tr;q=0.9,en-US;q=0.8,en;q=0.7',
#                                                                            'HTTP_COOKIE': 'csrftoken=pYTOrsEiPdANFEXpeR5byys9vyp1KCDk5gprVUDxSlVE0OTMD0QNtpyOvVDgaArl; sessionid=hqv75csqcrtjp2q9tp8ea31re5fcm72s',
#                                                                            'wsgi.input'
#                                                                            : < django.core.handlers.wsgi.LimitedStream
# object
# at
# 0x0000027842E74EB0 >, 'wsgi.errors': < _io.TextIOWrapper
# name = '<stderr>'
# mode = 'w'
# encoding = 'utf-8' >, 'wsgi.version': (1,
#                                        0), 'wsgi.run_once': False, 'wsgi.url_scheme': 'http', 'wsgi.multithread': True, 'wsgi.multiprocess': False, 'wsgi.file_wrapper': <
#
# class 'wsgiref.util.FileWrapper'>, 'CSRF_COOKIE': 'pYTOrsEiPdANFEXpeR5byys9vyp1KCDk5gprVUDxSlVE0OTMD0QNtpyOvVDgaArl'
#
# }, 'method': 'GET', 'content_type': 'text/plain', 'content_params': {}, '_stream': < django.core.handlers.wsgi.LimitedStream
# object
# at
# 0x0000027842E74EE0 >, '_read_started': False, 'resolver_match': ResolverMatch(func=post.views.my_posts, args=(),
#                                                                               kwargs={}, url_name='myposts',
#                                                                               app_names=['post'], namespaces=['post'],
#                                                                               route='myposts/myposts/'), 'COOKIES': {
#     'csrftoken': 'pYTOrsEiPdANFEXpeR5byys9vyp1KCDk5gprVUDxSlVE0OTMD0QNtpyOvVDgaArl',
#     'sessionid': 'hqv75csqcrtjp2q9tp8ea31re5fcm72s'}, 'session': < django.contrib.sessions.backends.db.SessionStore
# object
# at
# 0x0000027842E764A0 >, 'user': < SimpleLazyObject: < function
# AuthenticationMiddleware.process_request. < locals >.< lambda > at 0x0000027842E31630 >>,
#                                                               '_messages': < FallbackStorage: request = < WSGIRequest: GET
# '/myposts/myposts/' >>, 'csrf_processing_done': True}
