from flask import Flask, render_template, request, jsonify
import requests
from bs4 import BeautifulSoup
import pandas as pd
import os

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/scrape', methods=['POST'])
def scrape():
    url = request.form.get('url')
    selector = request.form.get('selector')
    
    if not url:
        return jsonify({'error': 'URL is required'}), 400
    
    try:
        # Kirim permintaan HTTP ke URL
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        response = requests.get(url, headers=headers, timeout=10)
        
        # Periksa apakah permintaan berhasil
        if response.status_code == 200:
            # Parse HTML content
            soup = BeautifulSoup(response.text, 'html.parser')
            
            result = []
            if selector:
                # Gunakan selector yang disediakan user
                elements = soup.select(selector)
                for element in elements:
                    result.append({
                        'text': element.get_text(strip=True),
                        'html': str(element)
                    })
            else:
                # Default: ambil semua paragraf
                paragraphs = soup.find_all('p')
                for p in paragraphs:
                    result.append({
                        'text': p.get_text(strip=True),
                        'html': str(p)
                    })
            
            # Simpan hasil ke CSV jika ada data
            if result:
                df = pd.DataFrame([item['text'] for item in result], columns=['Content'])
                csv_path = os.path.join('static', 'data', 'scraped_data.csv')
                os.makedirs(os.path.dirname(csv_path), exist_ok=True)
                df.to_csv(csv_path, index=False)
            
            return jsonify({
                'success': True,
                'data': result,
                'message': f'Successfully scraped {len(result)} elements'
            })
        else:
            return jsonify({
                'success': False,
                'message': f'Failed to access the page: {response.status_code}'
            }), 400
                
    except Exception as e:
        return jsonify({
            'success': False,
            'message': f'Error: {str(e)}'
        }), 500

if __name__ == '__main__':
    os.makedirs(os.path.join('static', 'data'), exist_ok=True)
    app.run(debug=True)