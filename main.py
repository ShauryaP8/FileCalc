import tkinter as tk

def format_size(size):
    """Formats the file size with the appropriate unit and rounding."""
    units = ['bytes', 'KB', 'MB', 'GB', 'TB']
    index = 0

    while size >= 1024 and index < len(units)-1:
        size /= 1024
        index += 1

    return f"{size:.2f} {units[index]}"

def show_image_fields():
    dimension_label.pack()
    dimension_entry.pack()
    color_depth_label.pack()
    color_depth_entry.pack()

def hide_image_fields():
    dimension_label.pack_forget()
    dimension_entry.pack_forget()
    color_depth_label.pack_forget()
    color_depth_entry.pack_forget()

def show_audio_fields():
    length_label.pack()
    length_entry.pack()
    sample_rate_label.pack()
    sample_rate_entry.pack()
    resolution_label.pack()
    resolution_entry.pack()

def hide_audio_fields():
    length_label.pack_forget()
    length_entry.pack_forget()
    sample_rate_label.pack_forget()
    sample_rate_entry.pack_forget()
    resolution_label.pack_forget()

def calculate_file_size():
    file_type = file_type_variable.get()

    if file_type == 'Image':
        dimensions = dimension_entry.get()
        color_depth = color_depth_entry.get()
        
        if dimensions and color_depth and (int(color_depth) >= 0):
            try:
                # Split the dimensions by 'x' and convert them to integers
                width, height = map(int, dimensions.split('x'))
                
                if width >= 0 and height >= 0:
                    # Calculate the file size
                    file_size = width * height * (int(color_depth) / 8)

                    # Format the file size
                    formatted_size = format_size(file_size)

                    # Display the file size
                    result_label.config(text=f"File size: {formatted_size}")
                    return
            except ValueError:
                pass
    elif file_type == 'Audio':
        length = length_entry.get()
        sample_rate = sample_rate_entry.get()
        resolution = resolution_entry.get()

        if length and sample_rate and resolution and (float(length) >= 0) and (int(sample_rate) >= 0) and (int(resolution) >= 0):
            try:
                length = float(length)
                sample_rate = int(sample_rate)
                resolution = int(resolution)

                # Calculate the file size
                file_size = length * sample_rate * resolution
                
                # Format the file size
                formatted_size = format_size(file_size)

                # Display the file size
                result_label.config(text=f"File size: {formatted_size}")
                return
            except ValueError:
                pass

    # Display the "Invalid input" message
    result_label.config(text="Invalid input")

def update_fields(*args):
    file_type = file_type_variable.get()

    if file_type == 'Image':
        show_image_fields()
        hide_audio_fields()
    elif file_type == 'Audio':
        show_audio_fields()
        hide_image_fields()

# Create a window
window = tk.Tk()
window.title('FileCalc')

# Create widgets
file_type_label = tk.Label(window, text="Select file type:")
file_type_label.pack()

file_type_variable = tk.StringVar(window)
file_type_variable.set('Image')  # Default value is 'Image'
file_type_variable.trace('w', update_fields)

file_type_dropdown = tk.OptionMenu(window, file_type_variable, 'Image', 'Audio')
file_type_dropdown.pack()

dimension_label = tk.Label(window, text="Enter dimensions (Width x Height):")
dimension_entry = tk.Entry(window)

color_depth_label = tk.Label(window, text="Enter color depth (in bits):")
color_depth_entry = tk.Entry(window)

length_label = tk.Label(window, text="Enter soundtrack length (in seconds):")
length_entry = tk.Entry(window)

sample_rate_label = tk.Label(window, text="Enter soundtrack sample rate (in Hz):")
sample_rate_entry = tk.Entry(window)

resolution_label = tk.Label(window, text="Enter soundtrack sample resolution (in bits):")
resolution_entry = tk.Entry(window)

button = tk.Button(window, text="Calculate", command=calculate_file_size)
button.pack()

result_label = tk.Label(window, text="")
result_label.pack()

# Start by showing image fields and hiding audio fields
show_image_fields()
hide_audio_fields()

# Start the GUI event loop
window.mainloop()
