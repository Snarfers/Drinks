//
//  ViewController.m
//  Drinks-Query
//
//  Created by Des Marks on 7/30/16.
//  Copyright © 2016 Des Marks. All rights reserved.
//

#import "ViewController.h"
#import "IngredientsRequest.h"

@interface ViewController ()
@property (weak, nonatomic) IBOutlet UITextView *TextBox;

@end

@implementation ViewController

- (void)viewDidLoad {
    [super viewDidLoad];
    // Do any additional setup after loading the view, typically from a nib.
}

- (void)didReceiveMemoryWarning {
    [super didReceiveMemoryWarning];
    // Dispose of any resources that can be recreated.
}
- (IBAction)RequestButton:(id)sender {
    IngredientsRequest *ingredientsQuery = [[IngredientsRequest alloc] init];
    
    NSMutableArray *queryItems = [[NSMutableArray alloc] initWithArray:@[@"ingredient/", @"all"]];
    
    self.TextBox.text = [ingredientsQuery getIngredientWithQueryParams:queryItems];
}
- (IBAction)ClearTextBoxButton:(id)sender {
    self.TextBox.text = nil;
}

@end
