
function add_to_db(e) {
				e.preventDefault();
				var data1= $('#Con').serialize()
				$.ajax({
					type: "POST", 
					url: "/compare/add-to-db", 
					data: $('#Con').serialize(),
					success: function(data){
						
						var d1 = $.parseJSON(data);
						alert("Notification will be sent to you, whenever the price falls");
						$('#Con').reset();
						return false;
					}
				})
			}
			
$("Con").submit(function(){
	e.preventDefault();
	add_to_db();
});