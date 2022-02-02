namespace Workshops
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
            this.workshopsListBox = new System.Windows.Forms.ListBox();
            this.locationsListBox = new System.Windows.Forms.ListBox();
            this.label1 = new System.Windows.Forms.Label();
            this.label2 = new System.Windows.Forms.Label();
            this.outputLabel = new System.Windows.Forms.Label();
            this.attendButton = new System.Windows.Forms.Button();
            this.exitButton = new System.Windows.Forms.Button();
            this.SuspendLayout();
            // 
            // workshopsListBox
            // 
            this.workshopsListBox.FormattingEnabled = true;
            this.workshopsListBox.Items.AddRange(new object[] {
            "Handling Stress",
            "Time Management",
            "Supervision Skills",
            "Negotiation",
            "How to Interview"});
            this.workshopsListBox.Location = new System.Drawing.Point(12, 30);
            this.workshopsListBox.Name = "workshopsListBox";
            this.workshopsListBox.Size = new System.Drawing.Size(105, 95);
            this.workshopsListBox.TabIndex = 0;
            // 
            // locationsListBox
            // 
            this.locationsListBox.FormattingEnabled = true;
            this.locationsListBox.Items.AddRange(new object[] {
            "Austin",
            "Chicago",
            "Dallas",
            "Orlando",
            "Phoenix",
            "Raleigh"});
            this.locationsListBox.Location = new System.Drawing.Point(169, 30);
            this.locationsListBox.Name = "locationsListBox";
            this.locationsListBox.Size = new System.Drawing.Size(67, 95);
            this.locationsListBox.TabIndex = 1;
            // 
            // label1
            // 
            this.label1.AutoSize = true;
            this.label1.Location = new System.Drawing.Point(12, 11);
            this.label1.Name = "label1";
            this.label1.Size = new System.Drawing.Size(61, 13);
            this.label1.TabIndex = 2;
            this.label1.Text = "Workshops";
            // 
            // label2
            // 
            this.label2.AutoSize = true;
            this.label2.Location = new System.Drawing.Point(166, 10);
            this.label2.Name = "label2";
            this.label2.Size = new System.Drawing.Size(53, 13);
            this.label2.TabIndex = 3;
            this.label2.Text = "Locations";
            // 
            // outputLabel
            // 
            this.outputLabel.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D;
            this.outputLabel.Font = new System.Drawing.Font("Courier New", 8.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.outputLabel.Location = new System.Drawing.Point(12, 128);
            this.outputLabel.Name = "outputLabel";
            this.outputLabel.Size = new System.Drawing.Size(267, 48);
            this.outputLabel.TabIndex = 4;
            // 
            // attendButton
            // 
            this.attendButton.Location = new System.Drawing.Point(12, 191);
            this.attendButton.Name = "attendButton";
            this.attendButton.Size = new System.Drawing.Size(75, 23);
            this.attendButton.TabIndex = 5;
            this.attendButton.Text = "Calculate";
            this.attendButton.UseVisualStyleBackColor = true;
            this.attendButton.Click += new System.EventHandler(this.attendButton_Click);
            // 
            // exitButton
            // 
            this.exitButton.Location = new System.Drawing.Point(204, 191);
            this.exitButton.Name = "exitButton";
            this.exitButton.Size = new System.Drawing.Size(75, 23);
            this.exitButton.TabIndex = 6;
            this.exitButton.Text = "Exit";
            this.exitButton.UseVisualStyleBackColor = true;
            this.exitButton.Click += new System.EventHandler(this.exitButton_Click);
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(286, 221);
            this.Controls.Add(this.exitButton);
            this.Controls.Add(this.attendButton);
            this.Controls.Add(this.outputLabel);
            this.Controls.Add(this.label2);
            this.Controls.Add(this.label1);
            this.Controls.Add(this.locationsListBox);
            this.Controls.Add(this.workshopsListBox);
            this.Name = "Form1";
            this.Text = "Form1";
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.ListBox workshopsListBox;
        private System.Windows.Forms.ListBox locationsListBox;
        private System.Windows.Forms.Label label1;
        private System.Windows.Forms.Label label2;
        private System.Windows.Forms.Label outputLabel;
        private System.Windows.Forms.Button attendButton;
        private System.Windows.Forms.Button exitButton;
    }
}

