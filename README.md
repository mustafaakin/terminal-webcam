# Terminal Webcam

This project captures images from your webcam and displays them in the terminal. There are two versions of the script: `capture.py` which displays monochrome webcam output, and `color.py` which displays colored webcam output.

<!-- image 500x500 -->
<img src="./monochrome_example.png" alt="Monochrome Example" width="500"/>
<!-- ![Monochrome Example](./monochrome_example.png) -->

**Monochrome Example**

<img src="./colored_example.png" alt="Colored Example" width="500"/>
<!-- ![Colored Example](./colored_example.png) -->

**Colored Example**

## Running the project

This project is meant to be run on Linux. Follow the steps below to set it up:

1. First, clone the repository:

```
git clone https://github.com/mustafaakin/terminal-webcam.git
```

2. Navigate into the project directory:

```
cd terminal-webcam
```

3. Create a virtual environment using `venv`:

```
python3 -m venv venv
```

This will create a new directory `venv` in your project where all the dependencies will be installed.

4. Activate the virtual environment:

```
source venv/bin/activate
```

5. Install the project dependencies from `requirements.txt`:

```
pip install -r requirements.txt
```

6. Run the scripts:

For monochrome webcam output:

```
python3 capture.py
```

For colored webcam output:

```
python3 color.py
```

To quit the application, press Ctrl + C in the terminal.

Note: You'll need a webcam connected to your computer for this to work. Enjoy using your webcam in the terminal!

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.
