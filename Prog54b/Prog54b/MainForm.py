import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._label1 = System.Windows.Forms.Label()
		self._textBox1 = System.Windows.Forms.TextBox()
		self._textBox2 = System.Windows.Forms.TextBox()
		self._textBox3 = System.Windows.Forms.TextBox()
		self._textBox4 = System.Windows.Forms.TextBox()
		self._button1 = System.Windows.Forms.Button()
		self._button2 = System.Windows.Forms.Button()
		self._button3 = System.Windows.Forms.Button()
		self._label2 = System.Windows.Forms.Label()
		self._label3 = System.Windows.Forms.Label()
		self.SuspendLayout()
		# 
		# label1
		# 
		self._label1.Font = System.Drawing.Font("Microsoft Sans Serif", 18, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label1.Location = System.Drawing.Point(96, 9)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(330, 54)
		self._label1.TabIndex = 0
		self._label1.Text = "Choose 4 numbers"
		self._label1.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# textBox1
		# 
		self._textBox1.Location = System.Drawing.Point(12, 66)
		self._textBox1.Name = "textBox1"
		self._textBox1.Size = System.Drawing.Size(100, 20)
		self._textBox1.TabIndex = 1
		# 
		# textBox2
		# 
		self._textBox2.Location = System.Drawing.Point(148, 66)
		self._textBox2.Name = "textBox2"
		self._textBox2.Size = System.Drawing.Size(100, 20)
		self._textBox2.TabIndex = 2
		# 
		# textBox3
		# 
		self._textBox3.Location = System.Drawing.Point(282, 66)
		self._textBox3.Name = "textBox3"
		self._textBox3.Size = System.Drawing.Size(100, 20)
		self._textBox3.TabIndex = 3
		# 
		# textBox4
		# 
		self._textBox4.Location = System.Drawing.Point(411, 66)
		self._textBox4.Name = "textBox4"
		self._textBox4.Size = System.Drawing.Size(100, 20)
		self._textBox4.TabIndex = 4
		# 
		# button1
		# 
		self._button1.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button1.Location = System.Drawing.Point(13, 270)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(132, 57)
		self._button1.TabIndex = 5
		self._button1.Text = "CALCULATE"
		self._button1.UseVisualStyleBackColor = True
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button2.Location = System.Drawing.Point(197, 270)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(132, 57)
		self._button2.TabIndex = 6
		self._button2.Text = "CLEAR"
		self._button2.UseVisualStyleBackColor = True
		self._button2.Click += self.Button2Click
		# 
		# button3
		# 
		self._button3.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button3.Location = System.Drawing.Point(379, 270)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(132, 57)
		self._button3.TabIndex = 7
		self._button3.Text = "Exit"
		self._button3.UseVisualStyleBackColor = True
		self._button3.Click += self.Button3Click
		# 
		# label2
		# 
		self._label2.Font = System.Drawing.Font("Microsoft Sans Serif", 14, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label2.Location = System.Drawing.Point(13, 110)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(369, 54)
		self._label2.TabIndex = 8
		self._label2.Text = "Sum of 4 numbers:"
		self._label2.TextAlign = System.Drawing.ContentAlignment.MiddleLeft
		# 
		# label3
		# 
		self._label3.Font = System.Drawing.Font("Microsoft Sans Serif", 14, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label3.Location = System.Drawing.Point(12, 181)
		self._label3.Name = "label3"
		self._label3.Size = System.Drawing.Size(369, 54)
		self._label3.TabIndex = 9
		self._label3.Text = "Average of 4 numbers:"
		self._label3.TextAlign = System.Drawing.ContentAlignment.MiddleLeft
		# 
		# MainForm
		# 
		self.ClientSize = System.Drawing.Size(523, 339)
		self.Controls.Add(self._label3)
		self.Controls.Add(self._label2)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Controls.Add(self._textBox4)
		self.Controls.Add(self._textBox3)
		self.Controls.Add(self._textBox2)
		self.Controls.Add(self._textBox1)
		self.Controls.Add(self._label1)
		self.Name = "MainForm"
		self.Text = "Prog54b"
		self.ResumeLayout(False)
		self.PerformLayout()


	def Button1Click(self, sender, e):
		num1 = int(self._textBox1.Text)
		num2 = int(self._textBox2.Text)
		num3 = int(self._textBox3.Text)
		num4 = int(self._textBox4.Text)
		
		Sum = num1 + num2 + num3 + num4
		average = Sum / 4
		
		self._label2.Text = "Sum of 4 numbers: " + str(Sum)
		self._label3.Text = "Average of 4 numbers: " + str(average)

	def Button2Click(self, sender, e):
		self._textBox1.Text = ""
		self._textBox2.Text = ""
		self._textBox3.Text = ""
		self._textBox4.Text = ""
		
		self._label2.Text = "Sum of 4 numbers: "
		self._label3.Text = "Average of 4 numbers: "

	def Button3Click(self, sender, e):
		Application.Exit()