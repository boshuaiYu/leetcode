# 哈希表

## 基础知识

哈希表是根据关键码的值而直接访问的数据结构，数组就是最为常见的哈希表类型

<font color ="LightPink">哈希表主要是用来快速判断一个元素是否出现在集合之中，属于用空间换取时间的方式</font>

将元素集合映射到哈希表上主要通过<font color ="LightPink">哈希函数</font>,而哈希函数一般是通过HashCode把元素转换为数值，通过某种运算，将元素映射到哈希表上的索引数字(通常方法是利用元素字符串ASCII码进行取余运算)

参考下图来源于：https://www.bilibili.com/video/BV1RQ4y1U7Sd/?spm_id_from=333.337.search-card.all.click&vd_source=1ea4618b60783ecde5702f73958bbca9
![img.png](img.png)
上图展示了两种哈希函数：

* 定义最大key值长度-1作为哈希表中最大的索引

  * 可以看出{"Beans“：1.85}在哈希表中index4的位置，而{”Corn“：2.38}和{”Rice":1.92}在哈希表index3的位置上
  * 在哈希表中添加元素，删除元素，获取元素的值都是O(1)的时间复杂度
  * 但对于index3位置上有两个键值对，这种情况称为<font color ="LightBlue">哈希碰撞现象</font>
  * 解决一般哈希碰撞现象可以采用拉链法，即将发生的元素存储为链表形式
    ![img_1.png](img_1.png)
  * 也可使用线性探测法，即依靠哈希表中的空位解决碰撞问题，前提保证tableSize > dataSize
    ![img_2.png](img_2.png)
* <font color ="LightPink">利用元素字符串ASCII码进行取余运算</font>
    * “Beans”,“Corn”,“Rice"的ASCII码分别为115,110,101
    * 分别对上述进行6取余，得到余数1,2,5
    * 即可将三个元素分别放到index1,index2,index5且长度为6的哈希表中

哈希表中的常见哈希结构可以参考文档:https://programmercarl.com/%E5%93%88%E5%B8%8C%E8%A1%A8%E7%90%86%E8%AE%BA%E5%9F%BA%E7%A1%80.html

---

## Day5

* [leetcode242](https://leetcode.cn/problems/valid-anagram/)有效的字母异构词：
