#include<iostream>
#include<vector>
#include<iterator>
#include<numeric>
#include<algorithm>

int main()
{
  //////////PART A///////////

  //define
  
  std::vector<int> v1(100);
  std::vector<int>v2(10);

  //initialize
  
  std::iota( std::begin(v1) , std::end(v1) , 1);
  std::iota( std::begin(v2) , std::end(v2) , 1);

  //display:
  
  std::cout<<"v1:---------------:"<<std::endl;
  copy(v1.begin(),v1.end(),std::ostream_iterator<int>(std::cout,"\n"));
  std::cout<<"v2----------------:"<<std::endl;
  copy(v2.begin(),v2.end(),std::ostream_iterator<int>(std::cout,"\n"));
  
  //////////PART B//////////
  
  v2.insert(v2.end() , v1.begin(),v1.end() );

  //display:
  
  std::cout<<"v2----------------:"<<std::endl;
  copy(v2.begin(),v2.end(),std::ostream_iterator<int>(std::cout,"\n"));

  /////////PART C/////////
  
  std::vector<int>old_vec(50);
  std::copy_if(v1.begin(),v1.end(),old_vec.begin(),[](int i){return (i%2==1);});
  
  //display:
  
  std::cout<<"old_vec----------------:"<<std::endl;
  copy(old_vec.begin(),old_vec.end(),std::ostream_iterator<int>(std::cout,"\n"));
  
  /////////PART D//////////

  std::vector<int>reverse_vec(100);
  std::reverse_copy(v1.begin(), v1.end(),reverse_vec.begin());
  
  //display:
  
  std::cout<<"rv----------------:"<<std::endl;
  copy(reverse_vec.begin(),reverse_vec.end(),std::ostream_iterator<int>(std::cout,"\n"));

  /////////PART E///////////

  sort(v2.begin(),v2.end());

  //display:

  std::cout<<"v2----------------:"<<std::endl;
  copy(v2.begin(),v2.end(),std::ostream_iterator<int>(std::cout,"\n"));
  
  return 0;
}
