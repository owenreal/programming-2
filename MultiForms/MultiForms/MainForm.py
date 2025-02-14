import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._button1 = System.Windows.Forms.Button()
		self._textBox1 = System.Windows.Forms.TextBox()
		self.SuspendLayout()
		# 
		# button1
		# 
		self._button1.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button1.Location = System.Drawing.Point(97, 117)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(154, 111)
		self._button1.TabIndex = 0
		self._button1.Text = "SHOW NEW FORM"
		self._button1.UseVisualStyleBackColor = True
		self._button1.Click += self.Button1Click
		# 
		# textBox1
		# 
		self._textBox1.Font = System.Drawing.Font("Microsoft Sans Serif", 14, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._textBox1.Location = System.Drawing.Point(12, 12)
		self._textBox1.Name = "textBox1"
		self._textBox1.Size = System.Drawing.Size(338, 29)
		self._textBox1.TabIndex = 1
		# 
		# MainForm
		# 
		self.ClientSize = System.Drawing.Size(362, 332)
		self.Controls.Add(self._textBox1)
		self.Controls.Add(self._button1)
		self.Name = "MainForm"
		self.Text = "MultiForms"
		self.ResumeLayout(False)
		self.PerformLayout()


	def Button1Click(self, sender, e):
		from Form1 import *
		msg = self._textBox1.Text
		form1 = Form1(self, msg)
		form1.Show()
		self.Hide()