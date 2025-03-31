import subprocess
import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "workflow")))

from flask import Flask, request, jsonify
from workflow.question_matching import find_similar_question
from workflow.file_process import unzip_folder
from workflow.function_definations_llm import function_definitions_objects_llm
from workflow.openai_api import  extract_parameters
from workflow.solution_functions import functions_dict

app = Flask(__name__)

API_Key = os.getenv("API_Key")

@app.route("/api/", methods=["POST"])
def process_file():
    question = request.form.get("question")
    file = request.files.get("file")  # Get the uploaded file (optional)
    
    try:
        matched_function, matched_description = find_similar_question(question)

        if file:
            temp_dir, file_names = unzip_folder(file)
        parameters = extract_parameters(
            str(question),
            function_definitions_llm=function_definitions_objects_llm[matched_function],
        )

        solution_function = functions_dict.get(
            str(matched_function), lambda parameters: "No matching function found"
        )

        if file:
            answer = solution_function(file, *parameters)
        else:
            answer = solution_function(*parameters)
        return jsonify({"answer": answer})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/redeploy', methods=['GET'])
def redeploy():
    subprocess.run(["../redeploy.sh"], shell=True)
    return "Redeployment triggered!", 200

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
