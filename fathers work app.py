from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.core.clipboard import Clipboard

letter = ['A', 'B', 'I']

class WorkAssistant(App):
    def build(self):
        self.icon="icon.png"
        self.num = 0
        self.name_input = TextInput(hint_text='Enter Name')
        self.odm1_input = TextInput(hint_text='Enter ODM 1')
        self.time_in_input = TextInput(hint_text='Enter Time In')
        self.odm2_input = TextInput(hint_text='Enter ODM 2')
        self.time_out_input = TextInput(hint_text='Enter Time Out')
        self.output_label = TextInput(multiline=True, readonly=True)
        
        leg_button = Button(text='Leg')
        leg_button.bind(on_press=self.on_leg_button_press)
        
        copy_button = Button(text='Copy to Clipboard')
        copy_button.bind(on_press=self.on_copy_button_press)
        
        clear_button = Button(text='Clear')
        clear_button.bind(on_press=self.on_clear_button_press)
        
        layout = BoxLayout(orientation='vertical')
        layout.add_widget(self.name_input)
        layout.add_widget(self.odm1_input)
        layout.add_widget(self.time_in_input)
        layout.add_widget(self.odm2_input)
        layout.add_widget(self.time_out_input)
        layout.add_widget(leg_button)
        layout.add_widget(copy_button)
        layout.add_widget(clear_button)
        layout.add_widget(self.output_label)
        
        return layout
    
    def on_leg_button_press(self, instance):
        odm1 = self.odm1_input.text
        odm2 = self.odm2_input.text
        time_in = self.time_in_input.text
        time_out = self.time_out_input.text
        
        if self.num < len(letter):
            self.output_label.text += f'{self.name_input.text}\n'
            self.output_label.text += f'Leg: {letter[self.num]}\n'
            self.output_label.text += f'ODM 1: {odm1}\n'
            self.output_label.text += f'Time In: {time_in}\n'
            self.output_label.text += f'ODM 2: {odm2}\n'
            self.output_label.text += f'Time Out: {time_out}\n\n'
            self.num += 1
        else:
            self.output_label.text += "No more letters in 'letter' list!\n"
    
    def on_copy_button_press(self, instance):
        output_text = self.output_label.text
        if output_text.strip():  
            Clipboard.copy(output_text)
            self.output_label.text += 'Copied to clipboard!\n'
        else:
            self.output_label.text += 'Nothing to copy!\n'
    
    def on_clear_button_press(self, instance):
        self.name_input.text = ''
        self.odm1_input.text = ''
        self.odm2_input.text = ''
        self.time_in_input.text = ''
        self.time_out_input.text = ''
        self.output_label.text = ''

if __name__ == '__main__':
    WorkAssistant().run()
