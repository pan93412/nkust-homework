//
//  ContentView.swift
//  Week3BundleApp
//
//  Created by Yi-Jyun Pan on 2024/9/24.
//

import SwiftUI

struct ContentView: View {
    let name = "潘奕濬"
    let studentId = "C111156103"
    let department = "智慧商務系"
    
    var body: some View {
        NavigationStack {
            NavigationLink("哈囉！") {
                VStack {
                    Text(name)
                        .fontDesign(.serif)
                        .font(Font.largeTitle.bold())
                    Text(description)
                }.navigationTitle("哈囉！")
            }.navigationTitle("Week3BundleApp")
        }
    }
    
    var description: String {
        get {
            "\(studentId) \(department)"
        }
    }
}

#Preview {
    ContentView()
}
