using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

/*
 * Name:                Ruben Nunez
 * Class and Section:   CS 313 01
 * Assignment:          Program Assignment 02
 * Due Date:            Monday, October 11, 2021
 * Program Description: The program calculates the the state sales tax, the county sales tax, the total sales tax,
 *                      and the total of the sale when the user enters the amount of a purchase. Then, it displays
 *                      the results.
*/

namespace Program_02
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }
        private void calculateButton_Click(object sender, EventArgs e)
        {
            decimal purchaseAmount, stateSalesTax, countySalesTax, totalSalesTax, total;

            try
            {
                purchaseAmount = decimal.Parse(amountTextBox.Text);
                stateSalesTax = purchaseAmount * 4 / 100;
                countySalesTax = purchaseAmount * 2 / 100;

                totalSalesTax = stateSalesTax + countySalesTax;

                total = purchaseAmount + totalSalesTax;


                amountLabel.Text = purchaseAmount.ToString("c");
                stateSalesTaxLabel.Text = stateSalesTax.ToString("c");
                countySalesTaxLabel.Text = countySalesTax.ToString("c");
                totalSalesTaxLabel.Text = totalSalesTax.ToString("c");
                totalLabel.Text = total.ToString("c");

            }
            catch
            {
                MessageBox.Show("Invalid data has been entered. Please try again.");
            }

            
        }

        private void exitButton_Click(object sender, EventArgs e)
        {
            this.Close();
        }

    }
}
