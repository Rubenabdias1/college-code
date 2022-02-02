namespace ChangeCalculator
{
    partial class Form1
    {
        /// <summary>
        /// Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// Clean up any resources being used.
        /// </summary>
        /// <param name="disposing">true if managed resources should be disposed; otherwise, false.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows Form Designer generated code

        /// <summary>
        /// Required method for Designer support - do not modify
        /// the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent()
        {
            this.label1 = new System.Windows.Forms.Label();
            this.label2 = new System.Windows.Forms.Label();
            this.amountTextBox = new System.Windows.Forms.TextBox();
            this.determineButton = new System.Windows.Forms.Button();
            this.label3 = new System.Windows.Forms.Label();
            this.quartersLabel = new System.Windows.Forms.Label();
            this.label5 = new System.Windows.Forms.Label();
            this.dimesLabel = new System.Windows.Forms.Label();
            this.label7 = new System.Windows.Forms.Label();
            this.nickelsLabel = new System.Windows.Forms.Label();
            this.label9 = new System.Windows.Forms.Label();
            this.centsLabel = new System.Windows.Forms.Label();
            this.exitButton = new System.Windows.Forms.Button();
            this.SuspendLayout();
            // 
            // label1
            // 
            this.label1.Font = new System.Drawing.Font("Microsoft Sans Serif", 9.75F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.label1.Location = new System.Drawing.Point(12, 9);
            this.label1.Name = "label1";
            this.label1.Size = new System.Drawing.Size(100, 23);
            this.label1.TabIndex = 0;
            this.label1.Text = "Change";
            // 
            // label2
            // 
            this.label2.Location = new System.Drawing.Point(12, 32);
            this.label2.Name = "label2";
            this.label2.Size = new System.Drawing.Size(112, 23);
            this.label2.TabIndex = 1;
            this.label2.Text = "Amount of Change:";
            // 
            // amountTextBox
            // 
            this.amountTextBox.Location = new System.Drawing.Point(128, 29);
            this.amountTextBox.Name = "amountTextBox";
            this.amountTextBox.Size = new System.Drawing.Size(100, 20);
            this.amountTextBox.TabIndex = 2;
            // 
            // determineButton
            // 
            this.determineButton.Location = new System.Drawing.Point(15, 58);
            this.determineButton.Name = "determineButton";
            this.determineButton.Size = new System.Drawing.Size(213, 23);
            this.determineButton.TabIndex = 3;
            this.determineButton.Text = "Determine Composition of Change";
            this.determineButton.UseVisualStyleBackColor = true;
            this.determineButton.Click += new System.EventHandler(this.determineButton_Click);
            // 
            // label3
            // 
            this.label3.Location = new System.Drawing.Point(12, 97);
            this.label3.Name = "label3";
            this.label3.Size = new System.Drawing.Size(46, 23);
            this.label3.TabIndex = 4;
            this.label3.Text = "Quarter:";
            this.label3.TextAlign = System.Drawing.ContentAlignment.MiddleLeft;
            // 
            // quartersLabel
            // 
            this.quartersLabel.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D;
            this.quartersLabel.Font = new System.Drawing.Font("Microsoft Sans Serif", 9.75F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.quartersLabel.Location = new System.Drawing.Point(64, 97);
            this.quartersLabel.Name = "quartersLabel";
            this.quartersLabel.Size = new System.Drawing.Size(45, 23);
            this.quartersLabel.TabIndex = 5;
            this.quartersLabel.TextAlign = System.Drawing.ContentAlignment.MiddleRight;
            // 
            // label5
            // 
            this.label5.Location = new System.Drawing.Point(131, 97);
            this.label5.Name = "label5";
            this.label5.Size = new System.Drawing.Size(46, 23);
            this.label5.TabIndex = 6;
            this.label5.Text = "Dimes:";
            this.label5.TextAlign = System.Drawing.ContentAlignment.MiddleLeft;
            // 
            // dimesLabel
            // 
            this.dimesLabel.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D;
            this.dimesLabel.Font = new System.Drawing.Font("Microsoft Sans Serif", 9.75F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.dimesLabel.Location = new System.Drawing.Point(183, 97);
            this.dimesLabel.Name = "dimesLabel";
            this.dimesLabel.Size = new System.Drawing.Size(45, 23);
            this.dimesLabel.TabIndex = 7;
            this.dimesLabel.TextAlign = System.Drawing.ContentAlignment.MiddleRight;
            // 
            // label7
            // 
            this.label7.Location = new System.Drawing.Point(12, 120);
            this.label7.Name = "label7";
            this.label7.Size = new System.Drawing.Size(46, 23);
            this.label7.TabIndex = 8;
            this.label7.Text = "Nickels:";
            this.label7.TextAlign = System.Drawing.ContentAlignment.MiddleLeft;
            // 
            // nickelsLabel
            // 
            this.nickelsLabel.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D;
            this.nickelsLabel.Font = new System.Drawing.Font("Microsoft Sans Serif", 9.75F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.nickelsLabel.Location = new System.Drawing.Point(64, 120);
            this.nickelsLabel.Name = "nickelsLabel";
            this.nickelsLabel.Size = new System.Drawing.Size(45, 23);
            this.nickelsLabel.TabIndex = 9;
            this.nickelsLabel.TextAlign = System.Drawing.ContentAlignment.MiddleRight;
            // 
            // label9
            // 
            this.label9.Location = new System.Drawing.Point(131, 120);
            this.label9.Name = "label9";
            this.label9.Size = new System.Drawing.Size(46, 23);
            this.label9.TabIndex = 10;
            this.label9.Text = "Cents:";
            this.label9.TextAlign = System.Drawing.ContentAlignment.MiddleLeft;
            // 
            // centsLabel
            // 
            this.centsLabel.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D;
            this.centsLabel.Font = new System.Drawing.Font("Microsoft Sans Serif", 9.75F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.centsLabel.Location = new System.Drawing.Point(183, 120);
            this.centsLabel.Name = "centsLabel";
            this.centsLabel.Size = new System.Drawing.Size(45, 23);
            this.centsLabel.TabIndex = 11;
            this.centsLabel.TextAlign = System.Drawing.ContentAlignment.MiddleRight;
            // 
            // exitButton
            // 
            this.exitButton.AccessibleRole = System.Windows.Forms.AccessibleRole.ButtonMenu;
            this.exitButton.Location = new System.Drawing.Point(153, 157);
            this.exitButton.Name = "exitButton";
            this.exitButton.Size = new System.Drawing.Size(75, 23);
            this.exitButton.TabIndex = 12;
            this.exitButton.Text = "Exit";
            this.exitButton.UseVisualStyleBackColor = true;
            this.exitButton.Click += new System.EventHandler(this.exitButton_Click);
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(241, 187);
            this.Controls.Add(this.exitButton);
            this.Controls.Add(this.centsLabel);
            this.Controls.Add(this.label9);
            this.Controls.Add(this.nickelsLabel);
            this.Controls.Add(this.label7);
            this.Controls.Add(this.dimesLabel);
            this.Controls.Add(this.label5);
            this.Controls.Add(this.quartersLabel);
            this.Controls.Add(this.label3);
            this.Controls.Add(this.determineButton);
            this.Controls.Add(this.amountTextBox);
            this.Controls.Add(this.label2);
            this.Controls.Add(this.label1);
            this.Name = "Form1";
            this.Text = "Change";
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.Label label1;
        private System.Windows.Forms.Label label2;
        private System.Windows.Forms.TextBox amountTextBox;
        private System.Windows.Forms.Button determineButton;
        private System.Windows.Forms.Label label3;
        private System.Windows.Forms.Label quartersLabel;
        private System.Windows.Forms.Label label5;
        private System.Windows.Forms.Label dimesLabel;
        private System.Windows.Forms.Label label7;
        private System.Windows.Forms.Label nickelsLabel;
        private System.Windows.Forms.Label label9;
        private System.Windows.Forms.Label centsLabel;
        private System.Windows.Forms.Button exitButton;
    }
}

