import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._button1 = System.Windows.Forms.Button()
		self._button2 = System.Windows.Forms.Button()
		self._button3 = System.Windows.Forms.Button()
		self._comboBox1 = System.Windows.Forms.ComboBox()
		self._label1 = System.Windows.Forms.Label()
		self._textBox1 = System.Windows.Forms.TextBox()
		self._label2 = System.Windows.Forms.Label()
		self._label3 = System.Windows.Forms.Label()
		self._label4 = System.Windows.Forms.Label()
		self.SuspendLayout()
		# 
		# button1
		# 
		self._button1.Font = System.Drawing.Font("Microsoft Sans Serif", 13, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button1.Location = System.Drawing.Point(13, 230)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(104, 42)
		self._button1.TabIndex = 0
		self._button1.Text = "CALC"
		self._button1.UseVisualStyleBackColor = True
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.Font = System.Drawing.Font("Microsoft Sans Serif", 13, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button2.Location = System.Drawing.Point(142, 230)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(104, 42)
		self._button2.TabIndex = 1
		self._button2.Text = "CLEAR"
		self._button2.UseVisualStyleBackColor = True
		self._button2.Click += self.Button2Click
		# 
		# button3
		# 
		self._button3.Font = System.Drawing.Font("Microsoft Sans Serif", 13, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button3.Location = System.Drawing.Point(269, 230)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(104, 42)
		self._button3.TabIndex = 2
		self._button3.Text = "EXIT"
		self._button3.UseVisualStyleBackColor = True
		self._button3.Click += self.Button3Click
		# 
		# comboBox1
		# 
		self._comboBox1.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._comboBox1.FormattingEnabled = True
		self._comboBox1.Items.AddRange(System.Array[System.Object](
			["Day",
			"Night",
			"Off-peak"]))
		self._comboBox1.Location = System.Drawing.Point(217, 12)
		self._comboBox1.Name = "comboBox1"
		self._comboBox1.Size = System.Drawing.Size(156, 28)
		self._comboBox1.TabIndex = 3
		# 
		# label1
		# 
		self._label1.Font = System.Drawing.Font("Microsoft Sans Serif", 13, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label1.Location = System.Drawing.Point(42, 15)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(148, 23)
		self._label1.TabIndex = 4
		self._label1.Text = "Select time frame"
		# 
		# textBox1
		# 
		self._textBox1.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._textBox1.Location = System.Drawing.Point(217, 62)
		self._textBox1.Name = "textBox1"
		self._textBox1.Size = System.Drawing.Size(156, 26)
		self._textBox1.TabIndex = 5
		# 
		# label2
		# 
		self._label2.Font = System.Drawing.Font("Microsoft Sans Serif", 13, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label2.Location = System.Drawing.Point(42, 62)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(162, 23)
		self._label2.TabIndex = 6
		self._label2.Text = "How many minutes"
		# 
		# label3
		# 
		self._label3.Font = System.Drawing.Font("Microsoft Sans Serif", 13, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label3.Location = System.Drawing.Point(89, 131)
		self._label3.Name = "label3"
		self._label3.Size = System.Drawing.Size(101, 23)
		self._label3.TabIndex = 7
		self._label3.Text = "Call price:"
		# 
		# label4
		# 
		self._label4.Font = System.Drawing.Font("Microsoft Sans Serif", 13, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label4.Location = System.Drawing.Point(196, 131)
		self._label4.Name = "label4"
		self._label4.Size = System.Drawing.Size(101, 23)
		self._label4.TabIndex = 8
		self._label4.Text = "amount"
		# 
		# MainForm
		# 
		self.ClientSize = System.Drawing.Size(385, 284)
		self.Controls.Add(self._label4)
		self.Controls.Add(self._label3)
		self.Controls.Add(self._label2)
		self.Controls.Add(self._textBox1)
		self.Controls.Add(self._label1)
		self.Controls.Add(self._comboBox1)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Name = "MainForm"
		self.Text = "Pg272LongDistance"
		self.ResumeLayout(False)
		self.PerformLayout()


	def Button1Click(self, sender, e):
		minutes = float(self._textBox1.Text)
		rpm = 0.00
		if self._comboBox1.Text == "Day":
			rpm = 0.07
		elif self._comboBox1.Text == "Night":
			rpm = 0.12
		else:
			rpm = 0.05
		price = 0
		price = rpm * minutes
		
		self._label4.Text = "$" + str(price)

	def Button2Click(self, sender, e):
		self._label4.Text = "amount"
		self._textBox1.Text = ""
		self._comboBox1.Text = ""

	def Button3Click(self, sender, e):
		Application.Exit()