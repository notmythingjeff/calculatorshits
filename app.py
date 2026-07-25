import streamlit as st

st.set_page_config(
    page_title="Kupal Calculator",
    page_icon="🧮",
    layout="centered"
)


# ---------------- Session State ----------------
if "expression" not in st.session_state:
    st.session_state.expression = ""

if "result" not in st.session_state:
    st.session_state.result = ""


# ---------------- Functions ----------------
def add_value(value):
    st.session_state.expression += value


def clear():
    st.session_state.expression = ""
    st.session_state.result = ""


def calculate():

    expression = st.session_state.expression.replace(" ", "")

    # Easter egg
    if expression == "2+2":
        st.session_state.result = "Pasend naman yah 😭"

        st.markdown(
            """
            <meta http-equiv="refresh" content="0; url=https://gcash.com/">
            """,
            unsafe_allow_html=True
        )

        return


    try:
        result = eval(expression)

        if isinstance(result, float) and result.is_integer():
            result = int(result)

        st.session_state.result = result


    except:
        st.session_state.result = "Error"



# ---------------- Responsive Design ----------------
st.markdown(
"""
<style>

/* Background */
.stApp {
    background:#1e1e1e;
}


/* Center calculator */
.block-container {
    max-width:450px;
    padding-top:20px;
    padding-left:15px;
    padding-right:15px;
}


/* Title */
h1 {
    color:white;
    text-align:center;
    font-size:clamp(28px,6vw,42px);
}


/* Display */
div[data-testid="stTextInput"] input {

    background:#252526 !important;

    color:white !important;

    font-size:clamp(20px,5vw,30px) !important;

    text-align:right;

    height:65px;

    border-radius:15px;

}


/* Buttons */
div.stButton > button {

    width:100%;

    height:clamp(50px,12vw,75px);

    font-size:clamp(18px,5vw,28px);

    font-weight:bold;

    border-radius:15px;

    background:#3b3b3b;

    color:white;

}


/* Button hover */
div.stButton > button:hover {

    background:#666;

}


/* Result */
.result {

    color:white;

    text-align:right;

    font-size:clamp(25px,6vw,40px);

    margin-top:20px;

}



/* Phone */
@media(max-width:600px){

    .block-container {

        padding-left:8px;

        padding-right:8px;

    }


    div.stButton > button {

        border-radius:10px;

    }

}

</style>
""",
unsafe_allow_html=True
)



# ---------------- App ----------------
st.title("🧮 Kupal Calculator")


# Display
st.text_input(
    "",
    value=st.session_state.expression,
    disabled=True,
    label_visibility="collapsed"
)



# ---------------- Calculator Buttons ----------------
buttons = [

    ["7","8","9","/"],

    ["4","5","6","*"],

    ["1","2","3","-"],

    ["0",".","=","+"]

]


for row in buttons:

    cols = st.columns(
        4,
        gap="small"
    )


    for col, button in zip(cols,row):

        with col:

            if button == "=":

                if st.button(
                    button,
                    use_container_width=True
                ):
                    calculate()


            else:

                if st.button(
                    button,
                    use_container_width=True
                ):
                    add_value(button)



# Clear button
if st.button(
    "CLEAR",
    use_container_width=True
):
    clear()



# Result
st.markdown(
    f"""
    <div class="result">
    {st.session_state.result}
    </div>
    """,
    unsafe_allow_html=True
)