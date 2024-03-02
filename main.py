import streamlit as st
from login import show_login_page
from tela1 import show_tela1
from tela2 import show_tela2

def logout():
    st.session_state['logged_in'] = False
    st.experimental_rerun()

def main():
    if 'logged_in' not in st.session_state:
        st.session_state['logged_in'] = False

    if not st.session_state['logged_in']:
        login_success = show_login_page()
        if login_success:
            st.session_state['logged_in'] = True
            st.experimental_rerun()
    else:
        st.sidebar.title("Web App da Mentoria")
        if st.sidebar.button("Tela 1"):
            st.session_state['current_page'] = "Tela 1"
        if st.sidebar.button("Tela 2"):
            st.session_state['current_page'] = "Tela 2"
        if st.sidebar.button('Logout'):
            logout()

        # Renderizando a tela selecionada
        if 'current_page' in st.session_state:
            if st.session_state['current_page'] == "Tela 1":
                show_tela1()
            elif st.session_state['current_page'] == "Tela 2":
                show_tela2()

if __name__ == "__main__":
    main()
