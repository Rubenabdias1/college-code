namespace Program_02
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
            this.amountTextBox = new System.Windows.Forms.TextBox();
            this.label2 = new System.Windows.Forms.Label();
            this.amountLabel = new System.Windows.Forms.Label();
            this.label4 = new System.Windows.Forms.Label();
            this.stateSalesTaxLabel = new System.Windows.Forms.Label();
            this.label6 = new System.Windows.Forms.Label();
            this.countySalesTaxLabel = new System.Windows.Forms.Label();
            this.label8 = new System.Windows.Forms.Label();
            this.totalSalesTaxLabel = new System.Windows.Forms.Label();
            this.totalLabel = new System.Windows.Forms.Label();
            this.label11 = new System.Windows.Forms.Label();
            this.calculateButton = new System.Windows.Forms.Button();
            this.exitButton = new System.Windows.Forms.Button();
            this.SuspendLayout();
            // 
            // label1
            // 
            this.label1.Location = new System.Drawing.Point(12, 9);
            this.label1.Name = "label1";
            this.label1.Size = new System.Drawing.Size(126, 23);
            this.label1.TabIndex = 0;
            this.label1.Text = "Amount of the purchase:";
            this.label1.TextAlign = System.Drawing.ContentAlignment.MiddleRight;
            // 
            // amountTextBox
            // 
            this.amountTextBox.Location = new System.Drawing.Point(153, 11);
            this.amountTextBox.Name = "amountTextBox";
            this.amountTextBox.Size = new System.Drawing.Size(100, 20);
            this.amountTextBox.TabIndex = 1;
            // 
            // label2
            // 
            this.label2.Location = new System.Drawing.Point(12, 32);
            this.label2.Name = "label2";
            this.label2.Size = new System.Drawing.Size(126, 23);
            this.label2.TabIndex = 2;
            this.label2.Text = "Amount of the purchase:";
            this.label2.TextAlign = System.Drawing.ContentAlignment.MiddleRight;
            // 
            // amountLabel
            // 
            this.amountLabel.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D;
            this.amountLabel.Font = new System.Drawing.Font("Microsoft Sans Serif", 9.75F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.amountLabel.Location = new System.Drawing.Point(153, 34);
            this.amountLabel.Name = "amountLabel";
            this.amountLabel.Size = new System.Drawing.Size(100, 23);
            this.amountLabel.TabIndex = 3;
            // 
            // label4
            // 
            this.label4.Location = new System.Drawing.Point(12, 55);
            this.label4.Name = "label4";
            this.label4.Size = new System.Drawing.Size(126, 23);
            this.label4.TabIndex = 4;
            this.label4.Text = "State sales tax:";
            this.label4.TextAlign = System.Drawing.ContentAlignment.MiddleRight;
            // 
            // stateSalesTaxLabel
            // 
            this.stateSalesTaxLabel.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D;
            this.stateSalesTaxLabel.Font = new System.Drawing.Font("Microsoft Sans Serif", 9.75F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.stateSalesTaxLabel.Location = new System.Drawing.Point(153, 57);
            this.stateSalesTaxLabel.Name = "stateSalesTaxLabel";
            this.stateSalesTaxLabel.Size = new System.Drawing.Size(100, 23);
            this.stateSalesTaxLabel.TabIndex = 5;
            // 
            // label6
            // 
            this.label6.Location = new System.Drawing.Point(12, 78);
            this.label6.Name = "label6";
            this.label6.Size = new System.Drawing.Size(126, 23);
            this.label6.TabIndex = 6;
            this.label6.Text = "County sales tax:";
            this.label6.TextAlign = System.Drawing.ContentAlignment.MiddleRight;
            // 
            // countySalesTaxLabel
            // 
            this.countySalesTaxLabel.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D;
            this.countySalesTaxLabel.Font = new System.Drawing.Font("Microsoft Sans Serif", 9.75F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.countySalesTaxLabel.Location = new System.Drawing.Point(153, 80);
            this.countySalesTaxLabel.Name = "countySalesTaxLabel";
            this.countySalesTaxLabel.Size = new System.Drawing.Size(100, 23);
            this.countySalesTaxLabel.TabIndex = 7;
            // 
            // label8
            // 
            this.label8.Location = new System.Drawing.Point(12, 101);
            this.label8.Name = "label8";
            this.label8.Size = new System.Drawing.Size(126, 23);
            this.label8.TabIndex = 8;
            this.label8.Text = "Total sales tax:";
            this.label8.TextAlign = System.Drawing.ContentAlignment.MiddleRight;
            // 
            // totalSalesTaxLabel
            // 
            this.totalSalesTaxLabel.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D;
            this.totalSalesTaxLabel.Font = new System.Drawing.Font("Microsoft Sans Serif", 9.75F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.totalSalesTaxLabel.Location = new System.Drawing.Point(153, 103);
            this.totalSalesTaxLabel.Name = "totalSalesTaxLabel";
            this.totalSalesTaxLabel.Size = new System.Drawing.Size(100, 23);
            this.totalSalesTaxLabel.TabIndex = 9;
            // 
            // totalLabel
            // 
            this.totalLabel.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D;
            this.totalLabel.Font = new System.Drawing.Font("Microsoft Sans Serif", 9.75F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.totalLabel.Location = new System.Drawing.Point(153, 126);
            this.totalLabel.Name = "totalLabel";
            this.totalLabel.Size = new System.Drawing.Size(100, 23);
            this.totalLabel.TabIndex = 11;
            // 
            // label11
            // 
            this.label11.Location = new System.Drawing.Point(12, 124);
            this.label11.Name = "label11";
            this.label11.Size = new System.Drawing.Size(126, 23);
            this.label11.TabIndex = 10;
            this.label11.Text = "Total:";
            this.label11.TextAlign = System.Drawing.ContentAlignment.MiddleRight;
            // 
            // calculateButton
            // 
            this.calculateButton.Location = new System.Drawing.Point(38, 159);
            this.calculateButton.Name = "calculateButton";
            this.calculateButton.Size = new System.Drawing.Size(75, 23);
            this.calculateButton.TabIndex = 12;
            this.calculateButton.Text = "Calculate";
            this.calculateButton.UseVisualStyleBackColor = true;
            this.calculateButton.Click += new System.EventHandler(this.calculateButton_Click);
            // 
            // exitButton
            // 
            this.exitButton.Location = new System.Drawing.Point(162, 159);
            this.exitButton.Name = "exitButton";
            this.exitButton.Size = new System.Drawing.Size(75, 23);
            this.exitButton.TabIndex = 13;
            this.exitButton.Text = "Exit";
            this.exitButton.UseVisualStyleBackColor = true;
            this.exitButton.Click += new System.EventHandler(this.exitButton_Click);
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(269, 196);
            this.Controls.Add(this.exitButton);
            this.Controls.Add(this.calculateButton);
            this.Controls.Add(this.totalLabel);
            this.Controls.Add(this.label11);
            this.Controls.Add(this.totalSalesTaxLabel);
            this.Controls.Add(this.label8);
            this.Controls.Add(this.countySalesTaxLabel);
            this.Controls.Add(this.label6);
            this.Controls.Add(this.stateSalesTaxLabel);
            this.Controls.Add(this.label4);
            this.Controls.Add(this.amountLabel);
            this.Controls.Add(this.label2);
            this.Controls.Add(this.amountTextBox);
            this.Controls.Add(this.label1);
            this.Name = "Form1";
            this.Text = "Form1";
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.Label label1;
        private System.Windows.Forms.TextBox amountTextBox;
        private System.Windows.Forms.Label label2;
        private System.Windows.Forms.Label amountLabel;
        private System.Windows.Forms.Label label4;
        private System.Windows.Forms.Label stateSalesTaxLabel;
        private System.Windows.Forms.Label label6;
        private System.Windows.Forms.Label countySalesTaxLabel;
        private System.Windows.Forms.Label label8;
        private System.Windows.Forms.Label totalSalesTaxLabel;
        private System.Windows.Forms.Label totalLabel;
        private System.Windows.Forms.Label label11;
        private System.Windows.Forms.Button calculateButton;
        private System.Windows.Forms.Button exitButton;
    }
}

