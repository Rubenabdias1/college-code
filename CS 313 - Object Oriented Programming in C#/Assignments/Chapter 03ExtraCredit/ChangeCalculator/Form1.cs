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
 * Ruben Nunez
 * CS 313 01
 * Chapter 03 Extra Credit
 * Wednesday, October 20, 2021
 * This program calculates the number of coins that add up to a change from 0 through 99 cents that the user enters.
 */


namespace ChangeCalculator
{
    public partial class Form1 : Form
    {
        private const int quarter = 25;
        private const int dime = 10;
        private const int nickel = 5;
        private const int cent = 1;

        public Form1()
        {
            InitializeComponent();
        }

        private void determineButton_Click(object sender, EventArgs e)
        {
            try
            {
                int amountOfChange;
                int changeLeftToDistribute;
                int amountOfQuarters;
                int amountOfDimes;
                int amountOfNickels;


                amountOfChange = int.Parse(amountTextBox.Text);
                changeLeftToDistribute = amountOfChange;

                amountOfQuarters = changeLeftToDistribute / quarter;
                changeLeftToDistribute -= amountOfQuarters * quarter;

                amountOfDimes = changeLeftToDistribute / dime;
                changeLeftToDistribute -= amountOfDimes * dime;

                amountOfNickels = changeLeftToDistribute / nickel;
                changeLeftToDistribute -= amountOfNickels * nickel;
                

                quartersLabel.Text = amountOfQuarters.ToString();
                dimesLabel.Text = amountOfDimes.ToString();
                nickelsLabel.Text = amountOfNickels.ToString();
                centsLabel.Text = changeLeftToDistribute.ToString();

            }
            catch
            {
                MessageBox.Show("Invalid data has been entered.");
            }
        }

        private void exitButton_Click(object sender, EventArgs e)
        {
            this.Close();
        }
    }
}
