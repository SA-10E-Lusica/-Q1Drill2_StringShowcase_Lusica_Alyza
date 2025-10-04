# SA_ICT10_Q1Drill2_Lusica_Alyza
# Author: Alyza Lusica

from pyscript import when, display, document

@when("click", "#submit-btn")
def show_message(event):
    # Assign strings to variables
    name = document.querySelector("#name").value
    age = document.querySelector("#age").value
    school = document.querySelector("#school").value   
    quote = "\"Education is the key to success.\"" 
    divider = "\\--------------------------\\"

    document.querySelector("#output").innerText = ""

    message = f"""👤 Student Profile
    {divider}
    \tName   : {name}
    \tAge    : {age}
    \tSchool : {school}

    ✏️ Notes:
    {name} is currently {age} years old and studies at {school}.
    A wise person once said: {quote}

    This information was gathered through input fields and displayed using a multiline script in Python via PyScript
    """

    display(message, target="output")
