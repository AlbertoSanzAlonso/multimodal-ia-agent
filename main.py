from app.gradio_interface import create_interface

def main():

    interface = create_interface()
    interface.launch()

if __name__ == "__main__":
    main()
