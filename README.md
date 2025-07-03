# 🤖 RoboSpeaker

A simple Python text-to-speech application that converts your text input into spoken words using the `pyttsx3` library. Perfect for accessibility, learning, or just having fun with voice synthesis!

## 🚀 Features

- ✅ Convert text to speech
- ✅ Interactive command-line interface
- ✅ Continuous operation until you quit
- ✅ Cross-platform compatibility
- ✅ Lightweight and easy to use

## 📋 Requirements

- Python 3.x
- pyttsx3 library

## 🛠️ Installation

1. Clone the repository:
```bash
git clone https://github.com/Sudo-Aditya/RoboSpeaker.git
cd RoboSpeaker
```

2. Install required dependencies:
```bash
pip install pyttsx3
```

## 🎯 Usage

1. Run the script:
```bash
python main.py
```

2. Enter the text you want the robot to speak when prompted
3. Type `q` to quit the application

## 📖 Example

```
Welcome to RoboSpeaker 1.1 Created By Aditya
Enter what you want me to speak: Hello World!
Enter what you want me to speak: This is awesome!
Enter what you want me to speak: q
```

## 🔧 Customization

You can customize the voice properties by modifying the `pyttsx3` engine:

```python
# Change speech rate
engine.setProperty('rate', 150)

# Change voice
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)  # Female voice

# Change volume
engine.setProperty('volume', 0.9)
```

## 🎵 Use Cases

- **Accessibility**: Help visually impaired users
- **Learning**: Language pronunciation practice
- **Entertainment**: Fun voice synthesis
- **Automation**: Voice alerts and notifications

## 🤝 Contributing

Feel free to fork this project and submit pull requests for any improvements such as:
- Voice customization options
- GUI interface
- File input support
- Multiple language support

## 📄 License

This project is open source and available under the MIT License.

## 👨‍💻 Author

Created by **Aditya Naik** - [GitHub](https://github.com/Sudo-Aditya)

---

⭐ Don't forget to star this repository if you found it helpful!