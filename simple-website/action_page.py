import os

headers= ["Content-type: text/html"]
qs = os.environ['QUERY_STRING']



def sendAnswer():
    print '''
    <html>
        <body>
            <h1>That's nice color i like that too</h1>
        </body>
    </html>
    '''

if qs :
    sendAnswer()