using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using System.IO;
using Microsoft.VisualBasic;

/*
Ruben Nunez
CS 313 01
Final Project
Monday, December 13, 2021
This program outputs a hospital bill. It makes the user fill out the form with
its name, address, the number of days spent in the hospital, the amount of 
medication charges, the amount of surgical charges, the amount of lab fees, and 
the amount of physical rehabilitation charges. It calculates the staying charges,
the miscellaneous charges, and the total charges.

*/


namespace FinalProject
{
    public partial class Form1 : Form
    {
        private const decimal STAYING_FEE = 350m;
        string name;
        string address;
        public Form1()
        {
            InitializeComponent();
        }
        private void Form1_Load(object sender, EventArgs e)
        {
            askForName();
            askForAddress();
        }

        private void askForName()
        {
            string tempName = Interaction.InputBox("Enter the name of the patient");
            nameLabel.Text = tempName;
            name = tempName;
        }
        private void askForAddress()
        {
            string tempAddress = Interaction.InputBox("Enter the name of the patient");
            addressLabel.Text = tempAddress;
            address = tempAddress;
        }

        private decimal calcStayCharges (int daysSpent )
        {
            decimal stayCharges;

            stayCharges = STAYING_FEE * daysSpent;

            return stayCharges;
        }
        private decimal calcMiscCharges(decimal medicationCharges, decimal surgicalCharges, decimal labFees, decimal rehabilitationCharges )
        {
            decimal miscCharges;

            miscCharges = medicationCharges + surgicalCharges + labFees + rehabilitationCharges;

            return miscCharges;
        }
        private decimal calcTotalCharges(decimal stayingCharges, decimal miscCharges)
        {
            decimal totalCharges;

            totalCharges = stayingCharges + miscCharges;

            return totalCharges;
        }


        private void calculateButton_Click(object sender, EventArgs e)
        {
            try
            {
                StreamWriter outputFile;

                outputFile = File.CreateText("bill.txt");
                
                int daysSpent;
                decimal medicationCharges;
                decimal surgicalCharges;
                decimal labFees;
                decimal phisicalRehabilitationCharges;

                decimal stayCharges;
                decimal miscCharges;
                decimal totalCharges;
                string output;
                

                if (!(int.TryParse(daysSpentTextBox.Text, out daysSpent)))
                {
                    MessageBox.Show("Invalid input for days spent.");
                    return;

                }
                if (!(decimal.TryParse(medicalChargesTextBox.Text, out medicationCharges)))
                {
                    MessageBox.Show("Invalid input for medication charges.");
                    return;

                }
                if (!(decimal.TryParse(surgicalChargesTextBox.Text, out surgicalCharges)))
                {
                    MessageBox.Show("Invalid input for surgical charges.");
                    return;

                }
                if (!(decimal.TryParse(labFeesTextBox.Text, out labFees)))
                {
                    MessageBox.Show("Invalid input for lab fees.");
                    return;

                }
                if (!(decimal.TryParse(daysSpentTextBox.Text, out phisicalRehabilitationCharges)))
                {
                    MessageBox.Show("Invalid input for phisical rehabilitation charges.");
                    return;

                }

                stayCharges = calcStayCharges(daysSpent);
                miscCharges = calcMiscCharges(medicationCharges, surgicalCharges, labFees, phisicalRehabilitationCharges);
                totalCharges = calcTotalCharges(stayCharges, miscCharges);

                output = "Name:             " + name +
                  "\n" + "Address:          " + address +
                  "\n" +
                  "\n" + "Days in Hospital: " + daysSpent.ToString() +
                  "\n" + "Base Charges:     " + stayCharges.ToString("c") +
                  "\n" + "Misc Charges:     " + miscCharges.ToString("c") +
                  "\n" + "Total Charges:    " + totalCharges.ToString("c");

                outputLabel.Text = output;
                outputFile.WriteLine(output);
                outputFile.Close();
            }
            catch (Exception ex)
            {
                MessageBox.Show(ex.Message);
            }
        }

        private void nameLabel_Click(object sender, EventArgs e)
        {
            askForName();

        }
        private void addressLabel_Click(object sender, EventArgs e)
        {
            askForAddress();
        }
        private void exitButton_Click(object sender, EventArgs e)
        {
            this.Close();
        }

    }
}
