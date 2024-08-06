from flask import Flask, request, jsonify
import uuid
from bs4 import BeautifulSoup
import anthropic
import xml.etree.ElementTree as ET
from parameters import PROMPT_LR_GR, PROMPT_FLOW, PROMPT_SUGGESTION

app = Flask(__name__)

YOUR_API = ''
MODEL_NAME = 'claude-3-5-sonnet-20240620'

client = anthropic.Anthropic(api_key=YOUR_API)

def get_completion(prompt, system='', prefill=''):
    message = client.messages.create(
        model=MODEL_NAME,
        max_tokens=4096,
        temperature=0.0,
        messages=[
            {"role": "user", "content": prompt},
            {"role": "assistant", "content": prefill}
        ],
        system=system
    )
    return message.content[0].text

def generate_deterministic_uuid(number):
    namespace_uuid = uuid.UUID('12345678-1234-5678-1234-567812345678')
    number_bytes = int(number).to_bytes(8, byteorder='big', signed=False)
    deterministic_uuid = uuid.uuid5(namespace_uuid, number_bytes.hex())
    return deterministic_uuid

@app.route('/process', methods=['POST'])
def process_request():
    try:
        data = request.json
        if not data:
            return jsonify({"message": "Invalid input: No JSON data provided"}), 400
        
        input_text = data.get('input', '')
        type_task = data.get('type', '')
        result_url = data.get('result_url', '')  # URL to send results to

        if not input_text:
            return jsonify({"message": "Invalid input: 'input' field is required"}), 400
        if not type_task:
            return jsonify({"message": "Invalid input: 'type' field is required"}), 400

        TASK_CONTEXT = f""" Below is a IELTS essay:
        <input>
        {input_text}
        </input>"""

        # Combine elements to create the prompt
        prompt = f"""{PROMPT_LR_GR}\n\n{TASK_CONTEXT}"""

        if type_task == 'LR_GR':
            try:
                # Get completion from the model
                output = get_completion(prompt)
            except Exception as e:
                return jsonify({"message": "Error in model completion", "error": str(e)}), 500

            try:
                output = '<root>' + output + '</root>'
                root = ET.fromstring(output)

                soup = BeautifulSoup(output, 'html.parser')

                # Find all elements with an id attribute
                for element in soup.find_all(attrs={"id": True}):
                    # Extract the numerical id value
                    number = int(element['id'])
                    # Replace the id with a deterministic UUID
                    element['id'] = str(generate_deterministic_uuid(number))
                soup_string = str(soup)
                root_repair = ET.fromstring(soup_string)
                repair_text = root_repair.find('repair')

                # Select comments
                comments = []
                for explanation in root.findall('.//explanation'):
                    comment_id = explanation.attrib['id']
                    comment_text = explanation.text.strip()
                    comments.append({
                        "id": str(generate_deterministic_uuid(comment_id)),
                        "comment": comment_text
                    })
            except Exception as e:
                return jsonify({"message": "Error in processing output", "error": str(e)}), 500

            result = {
                "data": str(repair_text),
                "comments": str(comments)
            }
            # # Send results to another API endpoint
            # if result_url:
            #     try:
            #         response = requests.post(result_url, json=result)
            #         response.raise_for_status()  # Raise an exception for HTTP errors
            #         return jsonify({"message": "Results sent successfully", "status_code": response.status_code})
            #     except requests.RequestException as e:
            #         return jsonify({"message": "Failed to send results", "error": str(e)}), 500

            return jsonify(result)
        
        elif type_task == "FLOW" or type_task == "SUGGESTION":
            try:
                # Get completion from the model
                output = get_completion(prompt)
            except Exception as e:
                return jsonify({"message": "Error in model completion", "error": str(e)}), 500

            result = {
                "data": str(output)
            }
            # # Send results to another API endpoint
            # if result_url:
            #     try:
            #         response = requests.post(result_url, json=result)
            #         response.raise_for_status()  # Raise an exception for HTTP errors
            #         return jsonify({"message": "Results sent successfully", "status_code": response.status_code})
            #     except requests.RequestException as e:
            #         return jsonify({"message": "Failed to send results", "error": str(e)}), 500

            return jsonify(result)
        else:
            return jsonify({"message": "Invalid input: 'type' field must be 'LR_GR', 'FLOW', or 'SUGGESTION'"}), 400

    except Exception as e:
        return jsonify({"message": "An error occurred while processing the request", "error": str(e)}), 500



@app.route('/receive', methods=['POST'])
def receive_result():
    data = request.json

    # Log or process the received result
    print("Received result:", data)

    # You can also perform other actions like saving to a database or performing further processing

    return jsonify({"message": "Result received successfully"}), 200

if __name__ == '__main__':
    app.run(debug=True)
