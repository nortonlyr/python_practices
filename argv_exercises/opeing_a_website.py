import webbrowser,sys
if len(sys.argv)>1:
    address = ''.join(sys.argv[1:])
webbrowser.open('http://www.sinovision.net/portal.php?mod=center&cate=shangxun&page='+address)