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
Ruben Nunez
CS 313 01
Chapter 04 Extra Credit
Wednesday, November 10, 2021
This program allows a customer to choose one of the training company's
workshop and a desired location. Then, it computes the amount of money
to pay based on the lenght in days of the workshop, the lodging fee of
the chosen location, and the registration fee of the workshop. 
 */
namespace Workshops
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private const int HANDLING_STRESS_REGISTRATION_FEE = 1000;
        private const int HANDLING_STRESS_DAYS = 3;
        private const int TIME_MANAGEMENT_REGISTRATION_FEE = 800;
        private const int TIME_MANAGEMENT_DAYS = 3;
        private const int SUPERVISION_SKILLS_REGISTRATION_FEE = 1500;
        private const int SUPERVISION_SKILLS_DAYS = 3;
        private const int NEGOTIATION_REGISTRATION_FEE = 1300;
        private const int NEGOTIATION_DAYS = 5;
        private const int HOW_TO_INTERVIEW_REGISTRATION_FEE = 500;
        private const int HOW_TO_INTERVIEW_DAYS = 1;

        private const int AUSTIN_LODGING_FEE = 150;
        private const int CHICAGO_LODGING_FEE = 225;
        private const int DALLAS_LODGING_FEE = 175;
        private const int ORLANDO_LODGING_FEE = 300;
        private const int PHOENIX_LODGING_FEE = 175;
        private const int RALEIGH_LODGING_FEE = 150;



        private void attendButton_Click(object sender, EventArgs e)
        {
        
            if (workshopsListBox.SelectedIndex == -1)
            {
                MessageBox.Show("Select a Workshop");
                return;
            }
            
            if (locationsListBox.SelectedIndex == -1)
            {
                MessageBox.Show("Select a Location");
                return;
            }

            decimal registrationFee = 0,
                lodgingFee = 0,
                lodging = 0,
                total = 0;
            int days = 0;
            string output = "";

            switch (workshopsListBox.SelectedItem)
            {
                case "Handling Stress":
                    registrationFee = HANDLING_STRESS_REGISTRATION_FEE;
                    days = HANDLING_STRESS_DAYS;
                    break;
                case "Time Management":
                    registrationFee = TIME_MANAGEMENT_REGISTRATION_FEE;
                    days = TIME_MANAGEMENT_DAYS;
                    break;
                case "Supervision Skills":
                    registrationFee = SUPERVISION_SKILLS_REGISTRATION_FEE;
                    days = SUPERVISION_SKILLS_DAYS;
                    break;
                case "Negotiation":
                    registrationFee = NEGOTIATION_REGISTRATION_FEE;
                    days = NEGOTIATION_DAYS;
                    break;
                case "How to Interview":
                    registrationFee = HOW_TO_INTERVIEW_REGISTRATION_FEE;
                    days = HOW_TO_INTERVIEW_DAYS;
                    break;
      

            } 

            switch (locationsListBox.SelectedItem)
            {
                case "Austin":
                    lodgingFee = AUSTIN_LODGING_FEE;
                    break;
                case "Chicago":
                    lodgingFee = CHICAGO_LODGING_FEE;
                    break;
                case "Dallas":
                    lodgingFee = DALLAS_LODGING_FEE;
                    break;
                case "Orlando":
                    lodgingFee = ORLANDO_LODGING_FEE;
                    break;
                case "Phoenix":
                    lodgingFee = PHOENIX_LODGING_FEE;
                    break;
                case "Raleigh":
                    lodgingFee = RALEIGH_LODGING_FEE;
                    break;
            }

            lodging = lodgingFee * days;
            total = registrationFee + lodging ;

            output = "Registration: " + registrationFee.ToString("c") + "\n"
                    + "Lodging: " + lodgingFee.ToString("c") + " X " + days + " days"
                    + " = " + lodging.ToString("c") + "\n"
                    + "Total: " + total.ToString("c");

            outputLabel.Text = output;


        }

        private void exitButton_Click(object sender, EventArgs e)
        {
            this.Close();
        }
    }
}
