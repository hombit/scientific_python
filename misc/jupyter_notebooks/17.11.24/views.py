def super_cool_sin(request, **kwargs):
    """
    Sci python test function
    """
    from django.http import HttpResponse
    import matplotlib as mpl
    mpl.use('Agg')
    import matplotlib.pyplot as plt
    from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas

    uplim = float(request.GET.get('uplim', 4))

    plt.plot(np.linspace(0, uplim, 100), np.sin(np.linspace(0, uplim, 100)))

    canvas = FigureCanvas(plt.gcf())
    response = HttpResponse(content_type='image/png')
    canvas.print_png(response, bbox_inches='tight')
    plt.clf()
    plt.close()
    return response
