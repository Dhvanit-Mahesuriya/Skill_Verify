
import sys
import os

# Add the application directory to the path so we can import app
sys.path.append(os.path.abspath('e:/Antigravity/skillverify'))

from app import app

def diagnose():
    print("Diagnosis: Starting...")
    try:
        # Create a test client
        client = app.test_client()
        
        # turn off error catching so we see the exception
        app.config['TESTING'] = True
        app.config['DEBUG'] = True
        
        print(f"Diagnosis: Attempting to render template directly...")
        with app.app_context():
            from flask import render_template
            try:
                rendered = render_template('careers_cs.html')
                print("Diagnosis: Success! Template found and rendered.")
                print(f"Length: {len(rendered)}")
            except Exception as e:
                print(f"Diagnosis: Failed to render locally: {e}")
                import traceback
                traceback.print_exc()

        print(f"Diagnosis: Fetching /careers/cs via client...")
        response = client.get('/careers/cs')
        
        print(f"Diagnosis: Status Code: {response.status_code}")
        
        if response.status_code == 200:
            print("Diagnosis: Success! Page rendered correctly (at least on server side).")
            print("Prefix of content:")
            print(response.data[:200])
        else:
            print("Diagnosis: FAILED. Status code is not 200.")
            print(response.data)
            
    except Exception as e:
        print("\nDiagnosis: EXCEPTION CAUGHT!")
        print(e)
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    diagnose()
