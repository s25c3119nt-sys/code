#include "philo.h"

#include "philo.h"

static void	eat(t_philo *p)
{
	pthread_mutex_t	*first;
	pthread_mutex_t	*second;

	if (p->left < p->right)
	{
		first = p->left;
		second = p->right;
	}
	else
	{
		first = p->right;
		second = p->left;
	}

	pthread_mutex_lock(first);
	pthread_mutex_lock(second);

	ft_print(p, "is eating");

	pthread_mutex_lock(&p->data->meal_mutex);
	p->last_meal = ft_time();
	pthread_mutex_unlock(&p->data->meal_mutex);

	usleep(p->data->time_eat * 1000);

	pthread_mutex_unlock(first);
	pthread_mutex_unlock(second);
}

static void	ft_sleep(t_philo *p)
{
	ft_print(p, "is sleeping");
	usleep(p->data->time_sleep * 1000);
}

static void	ft_think(t_philo *p)
{
	ft_print(p, "is thinking");
	usleep(1000); // ← 重要：飢餓防止
}

void	*routine(void *arg)
{
	t_philo	*p;

	p = (t_philo *)arg;

	if (p->id % 2 == 0)
		usleep(1000);

	while (!get_stop(p->data))
	{
		ft_think(p);

		usleep(500); // ← 重要：競合緩和

		eat(p);

		if (get_stop(p->data))
			break ;

		ft_sleep(p);
	}
	return (NULL);
}