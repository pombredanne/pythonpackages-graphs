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

