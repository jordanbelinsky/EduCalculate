/////////////////////////////////////////////////////////////
//  File Name:          SecondViewController.swift         //
//  Application Name:   educ[alcul]ate                     //
//                                                         //
//  Created by Jordan Belinsky on 2019-05-12.              //
//  Copyright © 2019 Jordan Belinsky. All rights reserved. //
/////////////////////////////////////////////////////////////

import UIKit

class SecondViewController: UIViewController {
    
    // declare text field inputs
    @IBOutlet weak var cMInput: UITextField!
    @IBOutlet weak var fMInput: UITextField!
    @IBOutlet weak var wInput: UITextField!
    
    // declare UI labels
    @IBOutlet weak var markOutput: UILabel!
    @IBOutlet weak var version: UILabel!
    
    override func viewDidLoad() {
        super.viewDidLoad()
        
        // display version number
        version.text = "Version: 1.0~b0.1"
        
        // check for general taps around screen area to dismiss keyboard
        let tap: UITapGestureRecognizer = UITapGestureRecognizer(target: self, action: #selector(FirstViewController.dismissKeyboard))
        view.addGestureRecognizer(tap)
        
        // setup for numpad support
        cMInput.keyboardType = UIKeyboardType.numberPad
        fMInput.keyboardType = UIKeyboardType.numberPad
        wInput.keyboardType = UIKeyboardType.numberPad
    }

    // function to dismiss keyboard on tap
    @objc func dismissKeyboard() {
        // prompts view to resign first responder status
        view.endEditing(true)
    }
    
    func finalExam(current: Int, final: Int, weight: Int) -> Int {
        
        // decalre required variable
        var required: Double
        let currentWeight = 1 - weight
        
        required = Double((final - currentWeight * current) / weight)
        
        // return required value from function
        return Int(required)
    }
    
    @IBAction func calculateMark(_ sender: Any) {
        
        // first responder revokation
        cMInput.resignFirstResponder()
        fMInput.resignFirstResponder()
        wInput.resignFirstResponder()
        
        // convert string values to integers
        let currentMark = Int(cMInput.text!)
        let endMark = Int(fMInput.text!)
        let weighting = Int(wInput.text!)!/100
        
        // calculate the final mark
        var finalMark: Int
        finalMark = finalExam(current: currentMark!, final: endMark!, weight: weighting)
        
        markOutput.text = "The mark you need is: \(finalMark)%"
    }
    
}

