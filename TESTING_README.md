## Testing Readme
### Code validation:
- [CI Python Linter](https://pep8ci.herokuapp.com)
- [Javascript validator](https://jshint.com/)
- [HTML validator](https://validator.w3.org/)
- [CSS validator](https://jigsaw.w3.org/css-validator/)


### The results are organized by app:



![shop](https://res.cloudinary.com/dmvf3llw4/image/upload/v1683236460/shop_aq56os.jpg)

![watch repair](https://res.cloudinary.com/dmvf3llw4/image/upload/v1683236460/watch_repair_gyjwbb.jpg)

![profile](https://res.cloudinary.com/dmvf3llw4/image/upload/v1683236459/profile_rwxh9w.jpg)

![checkout](https://res.cloudinary.com/dmvf3llw4/image/upload/v1683236459/checkout_nnhcqv.jpg)

![cart](https://res.cloudinary.com/dmvf3llw4/image/upload/v1683236459/cart_xd0cxi.jpg)

![staff](https://res.cloudinary.com/dmvf3llw4/image/upload/v1683236459/staff_gaat5x.jpg)

![blog](https://res.cloudinary.com/dmvf3llw4/image/upload/v1683236459/blog_mtixih.jpg)

![home](https://res.cloudinary.com/dmvf3llw4/image/upload/v1683236459/home_uny5qo.jpg)

### Browser Compatibility:
The site was tested on and in the following browsers, heres the results:

- Microsoft Edge - ✅
- Chrome - ✅
- Firefox - ✅
- Opera - ✅
- Safari - ✅

### The light house test:
![Light house test](https://res.cloudinary.com/dmvf3llw4/image/upload/v1683244538/ApplicationFrameHost_jD4Ouwctg9_pv5gcd.jpg)

![Light house test](https://res.cloudinary.com/dmvf3llw4/image/upload/v1683237787/ApplicationFrameHost_4vSYDnP8zV_hntje1.jpg)


## Manual Testing

![global](https://res.cloudinary.com/dmvf3llw4/image/upload/v1683238046/soffice.bin_8Gf1ar2BMU_p6agme.jpg)

![home](https://res.cloudinary.com/dmvf3llw4/image/upload/v1683236389/homee_ayokal.jpg)

![blog](https://res.cloudinary.com/dmvf3llw4/image/upload/v1683236389/blogg_yn1s2s.jpg)

![checkout](https://res.cloudinary.com/dmvf3llw4/image/upload/v1683236389/checkoutt_vi4kxr.jpg)

![shop](https://res.cloudinary.com/dmvf3llw4/image/upload/v1683244353/soffice.bin_bHk4aopUb8_xblzbn.jpg)

![about](https://res.cloudinary.com/dmvf3llw4/image/upload/v1683236388/aboutuss_tieuhb.jpg)

![watch repair](https://res.cloudinary.com/dmvf3llw4/image/upload/v1683236388/watchrepairr_jccv18.jpg)

## Known bugs
During manual testing, a bug was discovered where when a staff member deletes a product from the shop, the product would still remain in a user's session-data if it was added to their cart. 
I added some more code to the "delete product" view and looped over the items in the cart session, if the item matched the id of the deleted item it was then deleted from the session.
No other bugs are known.
