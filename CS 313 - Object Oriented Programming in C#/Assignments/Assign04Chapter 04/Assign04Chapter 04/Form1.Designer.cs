namespace Assign04Chapter_04
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
            this.burgersCheckBox = new System.Windows.Forms.CheckBox();
            this.friesCheckBox = new System.Windows.Forms.CheckBox();
            this.drinksCheckBox = new System.Windows.Forms.CheckBox();
            this.burgersChoicesGroupBox = new System.Windows.Forms.GroupBox();
            this.baconCheeseBurgerRadioButton = new System.Windows.Forms.RadioButton();
            this.baconBurgerRadioButton = new System.Windows.Forms.RadioButton();
            this.cheeseBurgerRadioButton = new System.Windows.Forms.RadioButton();
            this.regularBurgerRadioButton = new System.Windows.Forms.RadioButton();
            this.friesChoicesGroupBox = new System.Windows.Forms.GroupBox();
            this.largeFriesRadioButton = new System.Windows.Forms.RadioButton();
            this.mediumFriesRadioButton = new System.Windows.Forms.RadioButton();
            this.smallFriesRadioButton = new System.Windows.Forms.RadioButton();
            this.drinksChoicesGroupBox = new System.Windows.Forms.GroupBox();
            this.bottledWaterRadioButton = new System.Windows.Forms.RadioButton();
            this.sodaRadioButton = new System.Windows.Forms.RadioButton();
            this.computeButton = new System.Windows.Forms.Button();
            this.label1 = new System.Windows.Forms.Label();
            this.outputLabel = new System.Windows.Forms.Label();
            this.exitButton = new System.Windows.Forms.Button();
            this.outputListBox = new System.Windows.Forms.ListBox();
            this.burgersChoicesGroupBox.SuspendLayout();
            this.friesChoicesGroupBox.SuspendLayout();
            this.drinksChoicesGroupBox.SuspendLayout();
            this.SuspendLayout();
            // 
            // burgersCheckBox
            // 
            this.burgersCheckBox.AutoSize = true;
            this.burgersCheckBox.Location = new System.Drawing.Point(12, 58);
            this.burgersCheckBox.Name = "burgersCheckBox";
            this.burgersCheckBox.Size = new System.Drawing.Size(62, 17);
            this.burgersCheckBox.TabIndex = 0;
            this.burgersCheckBox.Text = "Burgers";
            this.burgersCheckBox.UseVisualStyleBackColor = true;
            this.burgersCheckBox.CheckedChanged += new System.EventHandler(this.burgersCheckBox_CheckedChanged);
            // 
            // friesCheckBox
            // 
            this.friesCheckBox.AutoSize = true;
            this.friesCheckBox.Location = new System.Drawing.Point(12, 182);
            this.friesCheckBox.Name = "friesCheckBox";
            this.friesCheckBox.Size = new System.Drawing.Size(48, 17);
            this.friesCheckBox.TabIndex = 1;
            this.friesCheckBox.Text = "Fries";
            this.friesCheckBox.UseVisualStyleBackColor = true;
            this.friesCheckBox.CheckedChanged += new System.EventHandler(this.friesCheckBox_CheckedChanged);
            // 
            // drinksCheckBox
            // 
            this.drinksCheckBox.AutoSize = true;
            this.drinksCheckBox.Location = new System.Drawing.Point(12, 274);
            this.drinksCheckBox.Name = "drinksCheckBox";
            this.drinksCheckBox.Size = new System.Drawing.Size(56, 17);
            this.drinksCheckBox.TabIndex = 2;
            this.drinksCheckBox.Text = "Drinks";
            this.drinksCheckBox.UseVisualStyleBackColor = true;
            this.drinksCheckBox.CheckedChanged += new System.EventHandler(this.drinksCheckBox_CheckedChanged);
            // 
            // burgersChoicesGroupBox
            // 
            this.burgersChoicesGroupBox.Controls.Add(this.baconCheeseBurgerRadioButton);
            this.burgersChoicesGroupBox.Controls.Add(this.baconBurgerRadioButton);
            this.burgersChoicesGroupBox.Controls.Add(this.cheeseBurgerRadioButton);
            this.burgersChoicesGroupBox.Controls.Add(this.regularBurgerRadioButton);
            this.burgersChoicesGroupBox.Location = new System.Drawing.Point(140, 18);
            this.burgersChoicesGroupBox.Name = "burgersChoicesGroupBox";
            this.burgersChoicesGroupBox.Size = new System.Drawing.Size(200, 115);
            this.burgersChoicesGroupBox.TabIndex = 3;
            this.burgersChoicesGroupBox.TabStop = false;
            this.burgersChoicesGroupBox.Text = "Choices for Burgers";
            this.burgersChoicesGroupBox.Visible = false;
            // 
            // baconCheeseBurgerRadioButton
            // 
            this.baconCheeseBurgerRadioButton.AutoSize = true;
            this.baconCheeseBurgerRadioButton.Location = new System.Drawing.Point(3, 85);
            this.baconCheeseBurgerRadioButton.Name = "baconCheeseBurgerRadioButton";
            this.baconCheeseBurgerRadioButton.Size = new System.Drawing.Size(162, 17);
            this.baconCheeseBurgerRadioButton.TabIndex = 3;
            this.baconCheeseBurgerRadioButton.Text = "w/ Bacon and Cheese (5.39)";
            this.baconCheeseBurgerRadioButton.UseVisualStyleBackColor = true;
            // 
            // baconBurgerRadioButton
            // 
            this.baconBurgerRadioButton.AutoSize = true;
            this.baconBurgerRadioButton.Location = new System.Drawing.Point(3, 62);
            this.baconBurgerRadioButton.Name = "baconBurgerRadioButton";
            this.baconBurgerRadioButton.Size = new System.Drawing.Size(102, 17);
            this.baconBurgerRadioButton.TabIndex = 2;
            this.baconBurgerRadioButton.Text = "w/ Bacon (4.79)";
            this.baconBurgerRadioButton.UseVisualStyleBackColor = true;
            // 
            // cheeseBurgerRadioButton
            // 
            this.cheeseBurgerRadioButton.AutoSize = true;
            this.cheeseBurgerRadioButton.Location = new System.Drawing.Point(3, 39);
            this.cheeseBurgerRadioButton.Name = "cheeseBurgerRadioButton";
            this.cheeseBurgerRadioButton.Size = new System.Drawing.Size(107, 17);
            this.cheeseBurgerRadioButton.TabIndex = 1;
            this.cheeseBurgerRadioButton.Text = "w/ Cheese (4.79)";
            this.cheeseBurgerRadioButton.UseVisualStyleBackColor = true;
            // 
            // regularBurgerRadioButton
            // 
            this.regularBurgerRadioButton.AutoSize = true;
            this.regularBurgerRadioButton.Checked = true;
            this.regularBurgerRadioButton.Location = new System.Drawing.Point(3, 16);
            this.regularBurgerRadioButton.Name = "regularBurgerRadioButton";
            this.regularBurgerRadioButton.Size = new System.Drawing.Size(92, 17);
            this.regularBurgerRadioButton.TabIndex = 0;
            this.regularBurgerRadioButton.TabStop = true;
            this.regularBurgerRadioButton.Text = "Regular (4.19)";
            this.regularBurgerRadioButton.UseVisualStyleBackColor = true;
            // 
            // friesChoicesGroupBox
            // 
            this.friesChoicesGroupBox.Controls.Add(this.largeFriesRadioButton);
            this.friesChoicesGroupBox.Controls.Add(this.mediumFriesRadioButton);
            this.friesChoicesGroupBox.Controls.Add(this.smallFriesRadioButton);
            this.friesChoicesGroupBox.Location = new System.Drawing.Point(140, 139);
            this.friesChoicesGroupBox.Name = "friesChoicesGroupBox";
            this.friesChoicesGroupBox.Size = new System.Drawing.Size(200, 85);
            this.friesChoicesGroupBox.TabIndex = 0;
            this.friesChoicesGroupBox.TabStop = false;
            this.friesChoicesGroupBox.Text = "Choices for Fries";
            this.friesChoicesGroupBox.Visible = false;
            // 
            // largeFriesRadioButton
            // 
            this.largeFriesRadioButton.AutoSize = true;
            this.largeFriesRadioButton.Location = new System.Drawing.Point(6, 65);
            this.largeFriesRadioButton.Name = "largeFriesRadioButton";
            this.largeFriesRadioButton.Size = new System.Drawing.Size(82, 17);
            this.largeFriesRadioButton.TabIndex = 2;
            this.largeFriesRadioButton.Text = "Large (4.99)";
            this.largeFriesRadioButton.UseVisualStyleBackColor = true;
            // 
            // mediumFriesRadioButton
            // 
            this.mediumFriesRadioButton.AutoSize = true;
            this.mediumFriesRadioButton.Location = new System.Drawing.Point(6, 42);
            this.mediumFriesRadioButton.Name = "mediumFriesRadioButton";
            this.mediumFriesRadioButton.Size = new System.Drawing.Size(92, 17);
            this.mediumFriesRadioButton.TabIndex = 1;
            this.mediumFriesRadioButton.Text = "Medium (3.09)";
            this.mediumFriesRadioButton.UseVisualStyleBackColor = true;
            // 
            // smallFriesRadioButton
            // 
            this.smallFriesRadioButton.AutoSize = true;
            this.smallFriesRadioButton.Checked = true;
            this.smallFriesRadioButton.Location = new System.Drawing.Point(6, 19);
            this.smallFriesRadioButton.Name = "smallFriesRadioButton";
            this.smallFriesRadioButton.Size = new System.Drawing.Size(80, 17);
            this.smallFriesRadioButton.TabIndex = 0;
            this.smallFriesRadioButton.TabStop = true;
            this.smallFriesRadioButton.Text = "Small (2.39)";
            this.smallFriesRadioButton.UseVisualStyleBackColor = true;
            // 
            // drinksChoicesGroupBox
            // 
            this.drinksChoicesGroupBox.Controls.Add(this.bottledWaterRadioButton);
            this.drinksChoicesGroupBox.Controls.Add(this.sodaRadioButton);
            this.drinksChoicesGroupBox.Location = new System.Drawing.Point(140, 245);
            this.drinksChoicesGroupBox.Name = "drinksChoicesGroupBox";
            this.drinksChoicesGroupBox.Size = new System.Drawing.Size(200, 69);
            this.drinksChoicesGroupBox.TabIndex = 0;
            this.drinksChoicesGroupBox.TabStop = false;
            this.drinksChoicesGroupBox.Text = "Choices for Drinks";
            this.drinksChoicesGroupBox.Visible = false;
            // 
            // bottledWaterRadioButton
            // 
            this.bottledWaterRadioButton.AutoSize = true;
            this.bottledWaterRadioButton.Location = new System.Drawing.Point(6, 42);
            this.bottledWaterRadioButton.Name = "bottledWaterRadioButton";
            this.bottledWaterRadioButton.Size = new System.Drawing.Size(120, 17);
            this.bottledWaterRadioButton.TabIndex = 1;
            this.bottledWaterRadioButton.Text = "Bottled Water (1.49)";
            this.bottledWaterRadioButton.UseVisualStyleBackColor = true;
            // 
            // sodaRadioButton
            // 
            this.sodaRadioButton.AutoSize = true;
            this.sodaRadioButton.Checked = true;
            this.sodaRadioButton.Location = new System.Drawing.Point(6, 19);
            this.sodaRadioButton.Name = "sodaRadioButton";
            this.sodaRadioButton.Size = new System.Drawing.Size(80, 17);
            this.sodaRadioButton.TabIndex = 0;
            this.sodaRadioButton.TabStop = true;
            this.sodaRadioButton.Text = "Soda (1.69)";
            this.sodaRadioButton.UseVisualStyleBackColor = true;
            // 
            // computeButton
            // 
            this.computeButton.Location = new System.Drawing.Point(444, 12);
            this.computeButton.Name = "computeButton";
            this.computeButton.Size = new System.Drawing.Size(83, 39);
            this.computeButton.TabIndex = 5;
            this.computeButton.Text = "Compute Cost of Meal";
            this.computeButton.UseVisualStyleBackColor = true;
            this.computeButton.Click += new System.EventHandler(this.computeButton_Click);
            // 
            // label1
            // 
            this.label1.AutoSize = true;
            this.label1.Location = new System.Drawing.Point(370, 189);
            this.label1.Name = "label1";
            this.label1.Size = new System.Drawing.Size(68, 13);
            this.label1.TabIndex = 6;
            this.label1.Text = "Cost of meal:";
            // 
            // outputLabel
            // 
            this.outputLabel.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D;
            this.outputLabel.Font = new System.Drawing.Font("Microsoft Sans Serif", 9.75F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.outputLabel.Location = new System.Drawing.Point(444, 186);
            this.outputLabel.Name = "outputLabel";
            this.outputLabel.Size = new System.Drawing.Size(147, 19);
            this.outputLabel.TabIndex = 7;
            this.outputLabel.TextAlign = System.Drawing.ContentAlignment.MiddleRight;
            // 
            // exitButton
            // 
            this.exitButton.Location = new System.Drawing.Point(516, 291);
            this.exitButton.Name = "exitButton";
            this.exitButton.Size = new System.Drawing.Size(75, 23);
            this.exitButton.TabIndex = 8;
            this.exitButton.Text = "Exit";
            this.exitButton.UseVisualStyleBackColor = true;
            this.exitButton.Click += new System.EventHandler(this.exitButton_Click);
            // 
            // outputListBox
            // 
            this.outputListBox.Font = new System.Drawing.Font("Courier New", 8.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.outputListBox.FormattingEnabled = true;
            this.outputListBox.ItemHeight = 14;
            this.outputListBox.Location = new System.Drawing.Point(373, 57);
            this.outputListBox.Name = "outputListBox";
            this.outputListBox.Size = new System.Drawing.Size(218, 116);
            this.outputListBox.TabIndex = 10;
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(603, 326);
            this.Controls.Add(this.outputListBox);
            this.Controls.Add(this.exitButton);
            this.Controls.Add(this.outputLabel);
            this.Controls.Add(this.label1);
            this.Controls.Add(this.computeButton);
            this.Controls.Add(this.drinksChoicesGroupBox);
            this.Controls.Add(this.friesChoicesGroupBox);
            this.Controls.Add(this.burgersChoicesGroupBox);
            this.Controls.Add(this.drinksCheckBox);
            this.Controls.Add(this.friesCheckBox);
            this.Controls.Add(this.burgersCheckBox);
            this.Name = "Form1";
            this.Text = "Restaurant Menu";
            this.burgersChoicesGroupBox.ResumeLayout(false);
            this.burgersChoicesGroupBox.PerformLayout();
            this.friesChoicesGroupBox.ResumeLayout(false);
            this.friesChoicesGroupBox.PerformLayout();
            this.drinksChoicesGroupBox.ResumeLayout(false);
            this.drinksChoicesGroupBox.PerformLayout();
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.CheckBox burgersCheckBox;
        private System.Windows.Forms.CheckBox friesCheckBox;
        private System.Windows.Forms.CheckBox drinksCheckBox;
        private System.Windows.Forms.GroupBox burgersChoicesGroupBox;
        private System.Windows.Forms.RadioButton baconCheeseBurgerRadioButton;
        private System.Windows.Forms.RadioButton baconBurgerRadioButton;
        private System.Windows.Forms.RadioButton cheeseBurgerRadioButton;
        private System.Windows.Forms.RadioButton regularBurgerRadioButton;
        private System.Windows.Forms.GroupBox friesChoicesGroupBox;
        private System.Windows.Forms.RadioButton largeFriesRadioButton;
        private System.Windows.Forms.RadioButton mediumFriesRadioButton;
        private System.Windows.Forms.RadioButton smallFriesRadioButton;
        private System.Windows.Forms.GroupBox drinksChoicesGroupBox;
        private System.Windows.Forms.RadioButton bottledWaterRadioButton;
        private System.Windows.Forms.RadioButton sodaRadioButton;
        private System.Windows.Forms.Button computeButton;
        private System.Windows.Forms.Label label1;
        private System.Windows.Forms.Label outputLabel;
        private System.Windows.Forms.Button exitButton;
        private System.Windows.Forms.ListBox outputListBox;
    }
}

