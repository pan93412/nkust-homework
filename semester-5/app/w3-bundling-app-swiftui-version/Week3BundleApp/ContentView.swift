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
            VStack {
                Text(name)
                    .fontDesign(.serif)
                    .font(Font.largeTitle.bold())
                Text(description)
                
                GeometryReader { geo in HStack(spacing: 0) {
                    Text("flex=0.3").frame(width: geo.size.width * 0.3).background(.red)
                    Text("flex=0.2").frame(width: geo.size.width * 0.2).background(.orange)
                    Text("flex=0.5").frame(width: geo.size.width * 0.5).background(.yellow)
                }.frame(
                    minWidth: 0,
                    maxWidth: .infinity
                ).border(.green)
                }
            }.navigationTitle("哈囉！")
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
