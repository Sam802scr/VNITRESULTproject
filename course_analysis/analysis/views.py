import numpy as np
from django.shortcuts import render
import base64
import io
import matplotlib.pyplot as plt
from django.conf import settings
import os
import pandas as pd
import matplotlib
matplotlib.use('Agg')


def load_csv(branch):
    filename = os.path.join(settings.BASE_DIR, 'data', f"{branch}_CGPA.csv")
    return pd.read_csv(filename)


def generate_histogram(df):
    plt.clf()
    plt.style.use('dark_background')
    plt.hist(df['CGPA'], bins=15, color='orange', rwidth=0.95)
    plt.xlabel('CGPA')
    plt.ylabel('Frequency')
    plt.title('Histogram Analysis of CGPA')
    plt.xticks(np.arange(5, 10, 0.5))

    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
    image_base64 = base64.b64encode(buf.read()).decode('utf-8')
    plt.close()

    return image_base64


def histogram_view(request):
    branch = request.GET.get('options', 'eee')  # Default to 'eee'
    try:
        df = load_csv(branch)
    except FileNotFoundError:
        return render(request, 'histogram.html', {'error': f'No data available for {branch}'})

    image_base64 = generate_histogram(df)
    return render(request, 'histogram.html', {'image_base64': image_base64})

# Create your views here.
