#from matplotlib.pyplot import clf
#from matplotlib.pyplot import figure
#from matplotlib.pyplot import pie
#from matplotlib.pyplot import savefig
#from matplotlib.pyplot import title


#@cache_region('one_hour')
#def percent_featured():
#    figsize = [8, 8]
#    np = num_packages(formatted=False)
#    npp = float(num_packages_pypi(
#        formatted=False))
#    if npp == 0:  # Don't divide by zero
#        npp = 1
#    percentage = np / npp
#    labels = (
#        'python\npackages\n.com (%s)' %
#            locale_format(int(np)),
#        'Python\nPackage\nIndex (%s)' %
#            locale_format(int(npp)),
#    )
#    figure(figsize=figsize)
#    pie([percentage, 1], labels=labels)
#    title(config.GRAPH_PERCENT_FEATURED_TITLE % (percentage * 100))
#    filename = os.path.join(config.HERE, 'static', 'img',
#        'graph_percent_featured.png')
#    savefig(filename, facecolor='#EEEEEE', format='png')
#    clf()


   ## Configure /graphs
    #config.add_route('vanity_graphs', '/graphs')
    #config.add_view('vanity_app.views.graphs',
    #    route_name='vanity_graphs',
    #        renderer='vanity_app:templates/vanity_graphs.mak')


# Graphs
#GRAPH_PERCENT_FEATURED_TITLE = '%2.f%% packages listed on Python \n'
#GRAPH_PERCENT_FEATURED_TITLE += 'Package Index featured on \n'
#GRAPH_PERCENT_FEATURED_TITLE += 'pythonpackages.com'


# View
#def graphs(request):  # Do this when someone requests '/graphs'
#    # Redir https
#    if request.headers.get('X-Forwarded-Proto') is not None:
#        if request.headers['X-Forwarded-Proto'] != 'https':
#            return HTTPMovedPermanently(location="https://%s%s" % (
#                request.host, request.path_qs))
#    # Check db
#    try:
#        utils.db.ping()
#    except:
#        return utils.get_default_response()
#    betacount = utils.get_beta_count()
#    followers = utils.get_followers()
#    fortune = utils.get_fortune()
#    utils.percent_featured()   # actually draw graph
#    num_downloads = utils.num_downloads()
#    num_packages = utils.num_packages()
#    num_packages_pypi = utils.num_packages_pypi()
#    num_times_featured = utils.num_times_featured()
#    num_downloads = utils.num_downloads()
#    userid = utils.get_authenticated_userid(request)
#    if userid is None:
#        menu = utils.get_not_logged_in()
#    else:
#        menu = utils.get_menu(userid)
#    # "New style" response. First initialize
#    # default, then populate values. 
#    response = utils.get_default_response()
#    if 'betacount' in response:
#        response['betacount'] = betacount
#    if 'followers' in response:
#        response['followers'] = followers
#    if 'fortune' in response:
#        response['fortune'] = fortune
#    if 'num_downloads' in response:
#        response['num_downloads'] = num_downloads
#    if 'num_packages' in response:
#        response['num_packages'] = num_packages
#    if 'num_packages_pypi' in response:
#        response['num_packages_pypi'] = num_packages_pypi
#    if 'num_times_featured' in response:
#        response['num_times_featured'] = num_times_featured
#    if 'num_downloads' in response:
#        response['num_downloads'] = num_downloads
#    if 'userid' in response:
#        response['userid'] = userid
#    if 'menu' in response:
#        response['menu'] = menu
#    return response
